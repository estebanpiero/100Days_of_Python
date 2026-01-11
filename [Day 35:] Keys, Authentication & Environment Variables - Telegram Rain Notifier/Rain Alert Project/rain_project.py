import requests
import os
from twilio.rest import Client   #Use to send SMS
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = os.getenv('OWM_WEB')
api_key = os.getenv('OWM_API_KEY')

twilio_account_id = os.getenv("TWILIO_ACCOUNT_ID")
twilio_token = os.getenv('TWILIO_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
my_number = os.getenv('USER_NUMBER')


MY_LATITUDE = 41.093990
MY_LONGITUDE = -74.145081

#MY_LATITUDE = 37.441883
#MY_LONGITUDE = -122.143021

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    'appid': api_key,
    'units':'imperial'
}

response = requests.get(OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data_sliced = weather_data['list'][:10]

will_rain = False

for id in weather_data_sliced:
    condition_code = id['weather'][0]['id']
    print(condition_code)
    if condition_code < 700:
        will_rain = True

if will_rain:
    
    client = Client(twilio_account_id,twilio_token)
    message = client.messages.create(
        body = "Bring an Umbrella",
        from_=f"whatsapp:{twilio_number}",
        to=f"whatsapp:{my_number}"
    )
    print(message.sid)
    print(message.status)
    print('Bring an umbrella')
