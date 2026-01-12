# validate_setup.py - Validate environment setup

import os
from dotenv import load_dotenv

def validate_setup():
    """Validate that all required environment variables are set"""
    
    load_dotenv()
    
    print("=" * 60)
    print("🔍 VALIDATING SETUP")
    print("=" * 60)
    
    required_vars = {
        'STOCK_API_KEY': 'Alpha Vantage API Key',
        'STOCK_WEB': 'Alpha Vantage API URL',
        'NEWS_API_KEY': 'News API Key',
        'NEWS_WEB': 'News API URL'
    }
    
    optional_vars = {
        'TWILIO_ACCOUNT_ID': 'Twilio Account ID (for SMS)',
        'TWILIO_TOKEN': 'Twilio Token (for SMS)',
        'TWILIO_NUMBER': 'Twilio Phone Number (for SMS)',
        'USER_NUMBER': 'Your Phone Number (for SMS)',
        'SMTP_SERVER': 'SMTP Server (for Email)',
        'SMTP_PORT': 'SMTP Port (for Email)',
        'SENDER_EMAIL': 'Sender Email',
        'SENDER_PASSWORD': 'Email Password',
        'RECEIVER_EMAIL': 'Receiver Email'
    }
    
    print("\n📋 Required Configuration:")
    all_required_set = True
    
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value:
            # Mask API keys for security
            if 'KEY' in var or 'TOKEN' in var:
                masked = value[:4] + '*' * (len(value) - 8) + value[-4:] if len(value) > 8 else '*' * len(value)
                print(f"  ✅ {description}: {masked}")
            else:
                print(f"  ✅ {description}: {value}")
        else:
            print(f"  ❌ {description}: NOT SET")
            all_required_set = False
    
    print("\n📋 Optional Configuration (for notifications):")
    
    for var, description in optional_vars.items():
        value = os.getenv(var)
        if value:
            if 'PASSWORD' in var or 'TOKEN' in var:
                print(f"  ✅ {description}: ********")
            else:
                print(f"  ✅ {description}: {value}")
        else:
            print(f"  ⚠️  {description}: NOT SET")
    
    print("\n" + "=" * 60)
    
    if all_required_set:
        print("✅ All required settings are configured!")
        print("You can now run: python main.py")
    else:
        print("❌ Missing required settings!")
        print("Please update your .env file with the missing values.")
        print("\nTo get API keys:")
        print("  - Alpha Vantage: https://www.alphavantage.co/support/#api-key")
        print("  - News API: https://newsapi.org/register")
    
    print("=" * 60)
    
    return all_required_set

if __name__ == "__main__":
    validate_setup()
