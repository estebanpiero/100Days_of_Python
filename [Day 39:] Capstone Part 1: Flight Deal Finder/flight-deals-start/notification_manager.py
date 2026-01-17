from twilio.rest import Client   #Use to send SMS
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_ID = os.getenv('TWILIO_ACCOUNT_ID')
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
MY_NUMBER = os.getenv('MY_NUMBER')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self,message):
        client = Client(TWILIO_ACCOUNT_ID,TWILIO_TOKEN)
        client.messages.create(
            body = message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
            )
        print(message.sid)
