# Price Tracker for Amazon Products

import smtplib
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
# Add as many products as you want: (url, target_price, product_name)
PRODUCTS = [
    {
        "name": "Mac Mini",
        "url": "https://www.amazon.com/dp/B0DLBVHSLD?th=1",
        "target_price": 1500.00,
    },
    {
        "name": "Example Keyboard",
        "url": "https://www.amazon.com/dp/EXAMPLE123",
        "target_price": 80.00,
    },
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/109.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7",
}


def get_price(url: str) -> float | None:
    """Fetch the current price of an Amazon product. Returns None if not found."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"  Request failed: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    price_element = soup.find("span", {"id": "apex-pricetopay-accessibility-label"})

    if not price_element:
        # Fallback selector used on some Amazon pages
        price_element = soup.find("span", class_="a-price-whole")

    if price_element:
        raw = price_element.text.strip().replace("$", "").replace(",", "").split()[0]
        try:
            return float(raw)
        except ValueError:
            print(f"  Could not parse price text: '{price_element.text.strip()}'")
    return None


def send_alert(alerts: list[dict]) -> None:
    """Send a single email listing all products below their target price."""
    my_email = os.getenv("MAIL_FROM")
    my_password = os.getenv("MAIL_PASSWORD")
    to_email = os.getenv("MAIL_TO")
    server = os.getenv("MAIL_SERVER")
    port = int(os.getenv("MAIL_PORT", 587))

    lines = []
    for item in alerts:
        lines.append(
            f"- {item['name']}: ${item['current_price']:.2f} "
            f"(target: ${item['target_price']:.2f})\n  {item['url']}"
        )

    body = (
        "Subject: Amazon Price Alert!\n\n"
        "The following products dropped below your target price:\n\n"
        + "\n\n".join(lines)
    )

    with smtplib.SMTP(server, port=port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=body)

    print(f"\nAlert email sent to {to_email} for {len(alerts)} product(s).")


def check_prices() -> None:
    alerts = []

    for product in PRODUCTS:
        print(f"Checking: {product['name']} ...")
        current_price = get_price(product["url"])

        if current_price is None:
            print("  Price not found — skipping.\n")
            continue

        print(f"  Current price : ${current_price:.2f}")
        print(f"  Target price  : ${product['target_price']:.2f}")

        if current_price < product["target_price"]:
            print("  --> BELOW TARGET! Adding to alert list.")
            alerts.append(
                {
                    "name": product["name"],
                    "url": product["url"],
                    "current_price": current_price,
                    "target_price": product["target_price"],
                }
            )
        else:
            print("  --> Above target, no alert needed.")
        print()

    if alerts:
        send_alert(alerts)
    else:
        print("No products are below their target price.")


if __name__ == "__main__":
    check_prices()
