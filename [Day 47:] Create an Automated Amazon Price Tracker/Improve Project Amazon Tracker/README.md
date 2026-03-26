# Amazon Price Tracker

A web-based Amazon price monitoring tool built with Python and Flask. Add products, set target prices, and get email alerts when a price drops — all from a live dashboard accessible from any device on your network.

---

## Features

- Add multiple Amazon products to track simultaneously
- Set an individual target price and notification email per product
- Live dashboard that updates in real time (no page refresh needed)
- Email alert sent automatically when a price drops below your target
- Edit target prices inline without removing and re-adding a product
- Accessible from any device on your local network

---

## How It Works

### Architecture

```
Browser  ──(HTTP)──►  Flask app (app.py)
                           │
                  ┌────────┴─────────┐
                  │                  │
           Background thread    SSE stream
           checks prices        pushes updates
           every N seconds      to all open tabs
                  │
           Amazon product page
           (web scraping via requests + BeautifulSoup)
```

### Price Checking

The app scrapes Amazon product pages using `requests` and `BeautifulSoup`. It tries several known CSS selectors in order to locate the price, since Amazon uses different layouts depending on the product and region.

### Real-Time Updates (Server-Sent Events)

The browser opens a persistent connection to `/stream`. Every time the background thread checks a price, the result is pushed to that connection as a JSON event — no polling required. This keeps the product table and the live log updated instantly on all connected devices.

### Email Alerts

When a product's current price drops below its target, an email is sent to the address you specified for that product. The alert fires **once per price-drop event** — it resets automatically if the price rises back above the target, so you will be notified again if it drops a second time.

---

## Project Structure

```
Improve Project Amazon Tracker/
├── app.py                        # Flask backend — routes, scraping, tracking thread, SSE
├── improved_amazon_price_tracker.py  # Original CLI version (kept for reference)
├── templates/
│   └── index.html                # Frontend — form, products table, live log
├── .env                          # Email credentials (you create this — not committed)
└── README.md                     # This file
```

---

## Setup

### 1. Install dependencies

```bash
pip install flask requests beautifulsoup4 python-dotenv
```

### 2. Create a `.env` file

Create a file called `.env` in the same folder as `app.py`:

```env
MAIL_FROM=your_sender@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
```

> **Gmail users:** you must use an [App Password](https://myaccount.google.com/apppasswords), not your regular account password. Enable 2-factor authentication first, then generate an app password for "Mail".

### 3. Run the app

```bash
python app.py
```

Open your browser at:

| Access | URL |
|--------|-----|
| This machine | http://127.0.0.1:5000 |
| Other devices on the same network | http://\<your-ip\>:5000 |

To find your local IP on Linux/macOS run `hostname -I`; on Windows run `ipconfig`.

---

## Usage

### Adding a product

1. Paste an Amazon product URL into the **Amazon URL** field.
2. Optionally give the product a name (e.g. "Mac Mini").
3. Enter your **target price** — you will be alerted when the price goes below this.
4. Enter the **email address** where you want to receive the alert.
5. Click **Add Product** or press Enter.

### Starting the tracker

1. Set the **check interval** (default: 60 seconds; minimum: 10 seconds).
2. Click **▶ Start Tracking**.
3. The status badge in the header turns green and the live log begins showing results.

### Editing a target price

Click the ✏️ icon next to any target price in the table. Type the new value and press **Enter** (or click ✔). Press **Escape** (or click ✖) to cancel. The change takes effect immediately and re-arms the email alert at the new threshold.

### Removing a product

Click the **Remove** button on any row. The product is removed from tracking immediately.

---

## Notes

- The tracker runs in a background thread inside Flask. It stops automatically when you click **■ Stop Tracking** or when the server is shut down. Product data is held in memory and is not persisted between restarts.
- Amazon's page structure occasionally changes, which can cause the scraper to fail to find the price. If a row shows an **Error** status, check that the URL is a valid Amazon product page and that the product is currently available.
- This uses Flask's built-in development server (`debug=True`), which is fine for personal/local use. Do not expose it to the public internet without a production WSGI server (e.g. Gunicorn) and a proper firewall.
