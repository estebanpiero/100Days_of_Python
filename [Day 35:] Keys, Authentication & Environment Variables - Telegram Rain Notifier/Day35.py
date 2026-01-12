# What is API Authentication?

# API Authentication is the process of verifying the identity of a user or application trying to access an API. 
# It ensures that only authorized users or applications can access the API's resources and perform actions.

# Common methods of API authentication include:

# 1. API Keys: A unique identifier that is passed along with API requests to identify the client.
# 2. OAuth: A token-based authentication method that allows users to grant third-party applications access to their resources without sharing their credentials.
# 3. JWT (JSON Web Tokens): A compact, URL-safe token that is used to securely transmit information between parties as a JSON object.
# 4. Basic Authentication: A simple method where the client sends a username and password with each request.
# 5. Bearer Tokens: A token that is sent in the HTTP Authorization header to authenticate API requests.

# Environment Variables:

# Environment variables are key-value pairs that are used to store configuration settings and sensitive information, such as API keys, database credentials, and other secrets. 
# They are typically set outside of the application code, allowing for better security and flexibility.
# Using environment variables helps to:
# 1. Keep sensitive information out of the source code.
# 2. Easily change configuration settings without modifying the code.
# 3. Manage different settings for different environments (development, testing, production).
# In Python, you can use the `os` module to access environment variables. For example:

import requests
import os
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv('OWM_API_KEY')

MY_LAT = 41.087  # Your latitude
MY_LONG = -74.131  # Your longitude

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

weather_request = requests.get(OWM_Endpoint, params=weather_params)
weather_request.raise_for_status()

weather_data = weather_request.json()

for hour_data in weather_data["list"]:
    print(hour_data["weather"][0]["id"])

print(hour_data["weather"][0]["id"])


