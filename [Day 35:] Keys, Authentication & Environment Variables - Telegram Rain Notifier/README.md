# Day 35: Keys, Authentication & Environment Variables - Telegram Rain Notifier

## Project: Rain Alert via Telegram

### Description
An automated weather monitoring service that sends Telegram notifications when rain is forecasted. Uses the OpenWeatherMap API with authentication and environment variables for security. Can be deployed to cloud services for 24/7 monitoring.

### What I Learned
- API authentication with API keys
- Environment variables for security
- Weather API integration
- Telegram bot creation and messaging
- Parsing weather data
- Cloud deployment concepts
- Scheduled automation

### How to Run
```bash
python3 main.py
```

### Features
- Weather forecast monitoring
- Rain detection (next 12 hours)
- Telegram notifications
- Secure API key storage
- Cloud deployment ready

### APIs Used

#### OpenWeatherMap API
```python
import requests

API_KEY = "your_api_key"
MY_LAT = 51.507351
MY_LON = -0.127758

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4,  # Next 12 hours (4 x 3-hour periods)
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)
data = response.json()
```

#### Telegram Bot API
```python
import requests

BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"

message = "Bring an umbrella! ☔"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
params = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, params=params)
```

### Weather Condition Codes
```python
# Rain condition codes (500-599)
weather_id = 500  # Light rain

will_rain = False
for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:  # Rain/snow
        will_rain = True
```

### Environment Variables

#### Setting Environment Variables

**Linux/Mac:**
```bash
export OWM_API_KEY="your_key"
export TELEGRAM_BOT_TOKEN="your_token"
export TELEGRAM_CHAT_ID="your_chat_id"
```

**Windows:**
```cmd
set OWM_API_KEY=your_key
```

#### Using in Python
```python
import os

API_KEY = os.environ.get("OWM_API_KEY")
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
```

### Creating a Telegram Bot

1. Message @BotFather on Telegram
2. Send `/newbot`
3. Choose name and username
4. Receive bot token
5. Start conversation with your bot
6. Get your chat ID using:
```
https://api.telegram.org/bot<TOKEN>/getUpdates
```

### Full Implementation
```python
import requests
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

MY_LAT = 51.507351
MY_LON = -0.127758

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

will_rain = False
for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    telegram_params = {
        "chat_id": CHAT_ID,
        "text": "It's going to rain today. Bring an umbrella! ☔"
    }
    requests.post(telegram_url, params=telegram_params)
```

### Weather Condition Code Ranges
- 200-299: Thunderstorm
- 300-399: Drizzle
- 500-599: Rain
- 600-699: Snow
- 700-799: Atmosphere (fog, etc.)
- 800: Clear
- 801-809: Clouds

### Key Concepts
- **API Keys**: Authentication for API access
- **Environment Variables**: Secure credential storage
- **Weather APIs**: Real-time weather data
- **Telegram Bots**: Automated messaging
- **Condition Codes**: Weather classification
- **Cloud Deployment**: Running 24/7 on servers

### Deployment Options
- PythonAnywhere (free tier available)
- Heroku
- AWS Lambda
- Google Cloud Functions
- Personal server with cron job

### Security Best Practices
1. Never hardcode API keys
2. Use environment variables
3. Add `.env` to `.gitignore`
4. Use different keys for dev/production
5. Rotate keys periodically

### Alternative: SMS Notifications
Can use Twilio API instead of Telegram:
```python
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="It's going to rain!",
    from_="+1234567890",
    to="+0987654321"
)
```

### Learning Focus
Professional API integration with proper security practices, environment variables, and automated notifications - essential for real-world applications.
