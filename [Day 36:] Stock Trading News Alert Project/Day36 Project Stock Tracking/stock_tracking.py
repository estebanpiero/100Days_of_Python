# Stock Price Tracking with alphavantage

import requests
import os
from twilio.rest import Client   # Use to send SMS
from dotenv import load_dotenv

load_dotenv()

STOCK_WEB = os.getenv('STOCK_WEB')
STOCK_API_KEY = os.getenv('STOCK_API_KEY')

NEWS_WEB = os.getenv('NEWS_WEB')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

twilio_account_id = os.getenv("TWILIO_ACCOUNT_ID")
twilio_token = os.getenv('TWILIO_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
my_number = os.getenv('USER_NUMBER')

# Initialize Twilio Client
client = Client(twilio_account_id, twilio_token)

# List of stocks to track
STOCKS = {
    'TSLA': 'tesla',
    'INTC': 'intel',
    'AAPL': 'apple',
    'NVDA': 'nvidia',
    'FTNT': 'fortinet',
    'AMD': 'amd',
    'SPY': 'spy'
}

# Threshold for price change alert (percentage)
ALERT_THRESHOLD = 1.0


def get_stock_data(symbol):
    """Fetch stock data from Alpha Vantage API"""
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': STOCK_API_KEY,
    }
    
    try:
        response = requests.get(STOCK_WEB, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Check for API errors
        if 'Error Message' in data:
            print(f"Error fetching {symbol}: {data['Error Message']}")
            return None
        if 'Note' in data:
            print(f"API limit reached: {data['Note']}")
            return None
            
        return data.get('Time Series (Daily)')
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None


def calculate_price_change(stock_data):
    """Calculate price difference and percentage"""
    data_list = [value for (key, value) in stock_data.items()]
    
    yesterday_closing_price = float(data_list[0]['4. close'])
    daybefore_closing_price = float(data_list[1]['4. close'])
    
    difference = yesterday_closing_price - daybefore_closing_price
    diff_percent = (abs(difference) / yesterday_closing_price) * 100
    
    # Determine if price went up or down
    direction = "🔺" if difference > 0 else "🔻"
    
    return {
        'yesterday': yesterday_closing_price,
        'daybefore': daybefore_closing_price,
        'difference': difference,
        'percent': diff_percent,
        'direction': direction
    }


def get_news(company_name):
    """Fetch news articles for the company"""
    news_param = {
        'apikey': NEWS_API_KEY,
        'qInTitle': company_name,
    }
    
    try:
        news_request = requests.get(NEWS_WEB, params=news_param)
        news_request.raise_for_status()
        news_data = news_request.json()['articles']
        return news_data[:3]  # Get only 3 articles
    except Exception as e:
        print(f"Error fetching news for {company_name}: {e}")
        return []


def send_sms(message):
    """Send SMS notification via Twilio"""
    try:
        message = client.messages.create(
            body=message,
            from_=f"whatsapp:{twilio_number}",
            to=f"whatsapp:{my_number}"
        )
        print(f"SMS sent successfully: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")


def format_alert_message(symbol, company_name, price_data, articles):
    """Format the alert message"""
    message = f"{symbol} {price_data['direction']}: {price_data['percent']:.2f}%\n"
    message += f"Yesterday: ${price_data['yesterday']:.2f}\n"
    message += f"Change: ${price_data['difference']:.2f}\n\n"
    
    if articles:
        message += "Top Headlines:\n"
        for i, article in enumerate(articles, 1):
            message += f"{i}. {article.get('title', 'No title')}\n"
    
    return message


# Main execution loop
print("=" * 50)
print("STOCK PRICE TRACKER - Multi-Stock Monitoring")
print("=" * 50)

for symbol, company_name in STOCKS.items():
    print(f"\nChecking {symbol} ({company_name.upper()})...")
    
    # Get stock data
    stock_data = get_stock_data(symbol)
    
    if not stock_data:
        continue
    
    # Calculate price changes
    price_data = calculate_price_change(stock_data)
    
    print(f"  Yesterday: ${price_data['yesterday']:.2f}")
    print(f"  Change: {price_data['direction']} ${abs(price_data['difference']):.2f} ({price_data['percent']:.2f}%)")
    
    # Check if change exceeds threshold
    if price_data['percent'] > ALERT_THRESHOLD:
        print(f"  ⚠️  ALERT: Price change exceeds {ALERT_THRESHOLD}% threshold!")
        
        # Get news
        articles = get_news(company_name)
        
        if articles:
            print(f"  📰 Found {len(articles)} news articles")
            for i, article in enumerate(articles, 1):
                print(f"     {i}. {article.get('title', 'No title')}")
        
        # Format and send SMS
        alert_message = format_alert_message(symbol, company_name, price_data, articles)
        send_sms(alert_message)
    else:
        print(f"  ✓ No significant change")

print("\n" + "=" * 50)
print("Stock monitoring complete!")
print("=" * 50)