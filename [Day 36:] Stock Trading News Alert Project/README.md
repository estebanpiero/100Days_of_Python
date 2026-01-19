# Day 36: Stock Trading News Alert Project

## Project: Stock Price Movement & News Alert

### Description
An automated stock monitoring system that tracks significant price movements and sends SMS/WhatsApp alerts with relevant news articles. When a stock price changes by 5% or more, the program fetches related news and sends notifications via Twilio.

### What I Learned
- Working with multiple APIs simultaneously
- Stock market data APIs
- News APIs
- SMS/WhatsApp messaging with Twilio
- Percentage calculations
- List slicing for top results
- Combining different data sources

### How to Run
```bash
python3 main.py
```

### Features
- Stock price monitoring
- 5% change threshold detection
- Related news article fetching
- SMS/WhatsApp notifications
- Multiple article alerts
- Up/down arrow indicators (🔺/🔻)

### APIs Used

#### 1. Alpha Vantage (Stock Prices)
```python
import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK = "TSLA"
API_KEY = "your_alpha_vantage_key"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
```

#### 2. News API
```python
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your_news_api_key"

news_params = {
    "q": "Tesla",  # or STOCK
    "apiKey": NEWS_API_KEY,
    "language": "en",
    "sortBy": "publishedAt"
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"][:3]  # Top 3
```

#### 3. Twilio (SMS/WhatsApp)
```python
from twilio.rest import Client

account_sid = "your_account_sid"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body=f"TSLA: 🔺5%\nHeadline: Tesla announces...",
    from_="+1234567890",  # Twilio number
    to="+0987654321"      # Your number
)
```

### Calculation Logic

```python
# Get last two closing prices
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_close = float(yesterday_data["4. close"])

day_before_yesterday = data_list[1]
dby_close = float(day_before_yesterday["4. close"])

# Calculate percentage difference
difference = yesterday_close - dby_close
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / yesterday_close) * 100)

# Check if significant change
if abs(diff_percent) > 5:
    # Fetch news and send alerts
```

### Full Implementation
```python
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha Vantage
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "your_key"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_close = float(data_list[0]["4. close"])
dby_close = float(data_list[1]["4. close"])

difference = yesterday_close - dby_close
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / yesterday_close) * 100)

if abs(diff_percent) > 5:
    # Get News
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = "your_news_key"

    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]

    # Send SMS
    TWILIO_SID = "your_sid"
    TWILIO_AUTH_TOKEN = "your_token"

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in articles:
        message = client.messages.create(
            body=f"{STOCK}: {up_down}{diff_percent}%\n"
                 f"Headline: {article['title']}\n"
                 f"Brief: {article['description']}",
            from_="whatsapp:+14155238886",  # Twilio Sandbox
            to="whatsapp:+1234567890"
        )
```

### Message Format
```
TSLA: 🔺5%
Headline: Tesla Announces Record Quarterly Deliveries
Brief: Tesla Inc reported record vehicle deliveries
in the third quarter...
```

### Key Concepts
- **Multiple APIs**: Coordinating data from different sources
- **Data Processing**: Extracting and calculating from JSON
- **List Comprehension**: Creating lists from dictionaries
- **List Slicing**: Getting top N items (`[:3]`)
- **Percentage Calculation**: Financial metrics
- **Conditional Alerts**: Threshold-based notifications

### API Setup Required

1. **Alpha Vantage**: Free API key at alphavantage.co
2. **News API**: Free API key at newsapi.org
3. **Twilio**: Account at twilio.com
   - For SMS: Get Twilio phone number
   - For WhatsApp: Use Twilio Sandbox

### Twilio WhatsApp Sandbox
1. Go to Twilio Console
2. Navigate to WhatsApp Sandbox
3. Send join message from WhatsApp
4. Use sandbox number for testing

### Automation
Schedule with:
- Cron (Linux/Mac)
- Task Scheduler (Windows)
- Cloud schedulers (AWS CloudWatch, etc.)

### Learning Focus
Integrating multiple APIs to create a sophisticated alert system for stock monitoring - practical application of API skills for financial automation.
