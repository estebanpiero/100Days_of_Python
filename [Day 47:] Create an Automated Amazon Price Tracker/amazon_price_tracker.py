#Price Tracker for Amazon Products

import smtplib
import requests
import time
import os
from bs4 import BeautifulSoup

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Email configuration from environment variables

def send_email(lower_price):
    my_email = os.getenv('MAIL_FROM')
    my_password = os.getenv('MAIL_PASSWORD')
    to_email = os.getenv('MAIL_TO')

    with smtplib.SMTP(os.getenv('MAIL_SERVER'), port=int(os.getenv('MAIL_PORT'))) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg='Subject:Price Alert!\n\n' \
            'The price of the product has dropped below your target price of ${:.2f}! Check it out: {}'.format(lower_price, mac_mini_url)
        )


# Amazon product URL (example: Mac Mini)

mac_mini_url = 'https://www.amazon.com/dp/B0DLBVHSLD?th=1'

# Headers to mimic a browser visit

HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7'
}

response = requests.get(mac_mini_url, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')

price_element = soup.find('span', {'id': 'apex-pricetopay-accessibility-label'})

print (price_element.text)

if price_element:
    price_text = price_element.text.strip()
    price_value = float(price_text.replace('$', '').replace(',', ''))
    print(f"Current price: ${price_value}")
    
    target_price = 1500.00  # Set your target price here
    
    if price_value < target_price:
        send_email(price_value)
else:
    print("Price element not found.")