"""
Amazon Price Tracker — Flask Web App
-------------------------------------
Run:  python app.py
Then open http://127.0.0.1:5000 in your browser.

Required .env variables (same folder):
  MAIL_FROM      sender email address
  MAIL_PASSWORD  sender email password / app-password
  MAIL_SERVER    e.g. smtp.gmail.com
  MAIL_PORT      e.g. 587
"""

import json
import os
import queue
import smtplib
import threading
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from flask import Flask, Response, jsonify, render_template, request, stream_with_context

load_dotenv()

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Scraping helpers
# ---------------------------------------------------------------------------

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/109.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7",
}

# Ordered list of CSS/ID selectors to try when looking for the price
PRICE_SELECTORS = [
    ("id", "apex-pricetopay-accessibility-label"),
    ("id", "priceblock_ourprice"),
    ("id", "priceblock_dealprice"),
    ("class", "a-price-whole"),
]


def get_price(url: str) -> tuple[float | None, str | None]:
    """Return (price_float, None) on success or (None, error_message) on failure."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=12)
        response.raise_for_status()
    except requests.RequestException as exc:
        return None, str(exc)

    soup = BeautifulSoup(response.text, "html.parser")

    for sel_type, sel_value in PRICE_SELECTORS:
        element = (
            soup.find("span", {"id": sel_value})
            if sel_type == "id"
            else soup.find("span", class_=sel_value)
        )
        if element:
            raw = element.text.strip().replace("$", "").replace(",", "").split()[0]
            try:
                return float(raw), None
            except ValueError:
                continue

    return None, "Price element not found on page"


# ---------------------------------------------------------------------------
# Email
# ---------------------------------------------------------------------------


def send_alert_email(product: dict, current_price: float) -> tuple[bool, str]:
    """Send a price-drop email. Returns (success, message)."""
    my_email = os.getenv("MAIL_FROM")
    my_password = os.getenv("MAIL_PASSWORD")
    server = os.getenv("MAIL_SERVER")
    port = int(os.getenv("MAIL_PORT", 587))
    to_email = product["notify_email"]

    subject = f"Price Alert: {product['name']} dropped to ${current_price:.2f}!"
    body = (
        f"Subject: {subject}\n\n"
        f"Great news! {product['name']} is now below your target price.\n\n"
        f"  Current price : ${current_price:.2f}\n"
        f"  Your target   : ${product['target_price']:.2f}\n\n"
        f"Buy it here: {product['url']}\n"
    )

    try:
        with smtplib.SMTP(server, port=port) as conn:
            conn.starttls()
            conn.login(user=my_email, password=my_password)
            conn.sendmail(from_addr=my_email, to_addrs=to_email, msg=body)
        return True, f"Alert sent to {to_email}"
    except Exception as exc:
        return False, f"Email failed: {exc}"


# ---------------------------------------------------------------------------
# In-memory state
# ---------------------------------------------------------------------------

products: dict[str, dict] = {}
product_lock = threading.Lock()

tracker_running = threading.Event()
tracker_thread: threading.Thread | None = None

# SSE — one Queue per connected browser tab
sse_clients: list[queue.Queue] = []


def broadcast(msg_type: str, data) -> None:
    """Push a JSON event to every connected SSE client."""
    message = json.dumps({"type": msg_type, "data": data})
    dead = []
    for q in sse_clients:
        try:
            q.put_nowait(message)
        except queue.Full:
            dead.append(q)
    for q in dead:
        sse_clients.remove(q)


def log(text: str) -> None:
    broadcast("log", {"time": time.strftime("%H:%M:%S"), "text": text})


# ---------------------------------------------------------------------------
# Background tracking thread
# ---------------------------------------------------------------------------


def tracking_loop(interval: int) -> None:
    log(f"Tracker started — checking every {interval}s.")
    broadcast("status", "running")

    while tracker_running.is_set():
        with product_lock:
            pids = list(products.keys())

        for pid in pids:
            if not tracker_running.is_set():
                break

            with product_lock:
                if pid not in products:
                    continue
                product = dict(products[pid])

            log(f"Checking: {product['name']} …")
            price, error = get_price(product["url"])
            checked_at = time.strftime("%H:%M:%S")

            with product_lock:
                if pid not in products:
                    continue
                p = products[pid]
                p["last_checked"] = checked_at

                if error:
                    p["status"] = "error"
                    p["error"] = error
                    log(f"  Error — {error}")
                else:
                    p["current_price"] = price
                    p["error"] = None

                    if price < product["target_price"]:
                        p["status"] = "below"
                        log(f"  BELOW TARGET  ${price:.2f} < ${product['target_price']:.2f}")
                        if not p.get("alert_sent"):
                            ok, msg = send_alert_email(p, price)
                            p["alert_sent"] = ok
                            log(f"  {msg}")
                    else:
                        p["status"] = "above"
                        p["alert_sent"] = False  # reset so alert fires again on next drop
                        log(f"  ${price:.2f}  (target ${product['target_price']:.2f})")

                broadcast("product_update", dict(p))

        # Wait for interval, waking each second to respect stop requests
        for _ in range(interval):
            if not tracker_running.is_set():
                break
            time.sleep(1)

    log("Tracker stopped.")
    broadcast("status", "stopped")


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products", methods=["GET"])
def list_products():
    with product_lock:
        return jsonify(list(products.values()))


@app.route("/products", methods=["POST"])
def add_product():
    data = request.json or {}
    url = data.get("url", "").strip()
    name = data.get("name", "").strip()
    notify_email = data.get("notify_email", "").strip()

    try:
        target_price = float(data.get("target_price", ""))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid target price"}), 400

    if not url or not notify_email:
        return jsonify({"error": "URL and email are required"}), 400

    pid = str(int(time.time() * 1000))
    if not name:
        name = f"Product {len(products) + 1}"

    entry = {
        "id": pid,
        "name": name,
        "url": url,
        "target_price": target_price,
        "notify_email": notify_email,
        "current_price": None,
        "status": "pending",
        "last_checked": None,
        "alert_sent": False,
        "error": None,
    }

    with product_lock:
        products[pid] = entry

    broadcast("product_added", entry)
    log(f"Added: {name} (target ${target_price:.2f})")
    return jsonify(entry), 201


@app.route("/products/<pid>", methods=["PATCH"])
def update_product(pid: str):
    data = request.json or {}
    try:
        new_price = float(data.get("target_price", ""))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid target price"}), 400

    with product_lock:
        if pid not in products:
            return jsonify({"error": "Not found"}), 404
        products[pid]["target_price"] = new_price
        products[pid]["alert_sent"] = False  # re-arm alert at new threshold
        entry = dict(products[pid])

    broadcast("product_update", entry)
    log(f"Updated target for {entry['name']}: ${new_price:.2f}")
    return jsonify(entry)


@app.route("/products/<pid>", methods=["DELETE"])
def remove_product(pid: str):
    with product_lock:
        if pid not in products:
            return jsonify({"error": "Not found"}), 404
        name = products[pid]["name"]
        del products[pid]

    broadcast("product_removed", {"id": pid})
    log(f"Removed: {name}")
    return jsonify({"success": True})


@app.route("/tracker/start", methods=["POST"])
def start_tracker():
    global tracker_thread

    data = request.json or {}
    interval = max(10, int(data.get("interval", 60)))

    with product_lock:
        if not products:
            return jsonify({"error": "Add at least one product first"}), 400

    if tracker_running.is_set():
        return jsonify({"error": "Tracker is already running"}), 400

    tracker_running.set()
    tracker_thread = threading.Thread(
        target=tracking_loop, args=(interval,), daemon=True
    )
    tracker_thread.start()
    return jsonify({"success": True, "interval": interval})


@app.route("/tracker/stop", methods=["POST"])
def stop_tracker():
    if not tracker_running.is_set():
        return jsonify({"error": "Tracker is not running"}), 400
    tracker_running.clear()
    log("Stop requested …")
    return jsonify({"success": True})


@app.route("/stream")
def stream():
    """Server-Sent Events endpoint — one persistent connection per browser tab."""

    def event_generator():
        q: queue.Queue = queue.Queue(maxsize=200)
        sse_clients.append(q)
        try:
            # Send the full current state to a newly connected client
            with product_lock:
                init_data = {
                    "products": list(products.values()),
                    "running": tracker_running.is_set(),
                }
            yield f"data: {json.dumps({'type': 'init', 'data': init_data})}\n\n"

            while True:
                try:
                    msg = q.get(timeout=25)
                    yield f"data: {msg}\n\n"
                except queue.Empty:
                    # Heartbeat keeps the connection alive through proxies
                    yield f"data: {json.dumps({'type': 'ping'})}\n\n"
        finally:
            if q in sse_clients:
                sse_clients.remove(q)

    return Response(
        stream_with_context(event_generator()),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
