import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_USERNAME = os.getenv('SHEETY_USERNAME')
SHEETY_PROJECT_NAME = os.getenv('SHEETY_PROJECT_NAME')
SHEETY_SHEET = 'users'
SHEETY_ENDPOINT = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET}/3'

AUTHORIZATION_HEADER = {
    'Authorization': f'Bearer {os.getenv("SHEETY_BEARER_TOKEN")}'
}

class UserDataBase():
    def __init__(self):
        print('Welcome to Flight Club\n')
        
        end_loop = False

        while not end_loop:
            self.firstname = input('What is your name: ')
            self.lastname = input('Whats your last name: ')
            self.email = input('Whats your email: ')
            self.emailconfirmation = input('Verify your email: ')
            
            if self.email != self.emailconfirmation:
                print('Wrong email provided')
            else:
                end_loop = True
                print('You are in the club')
                self.update_users_sheet()

    def update_users_sheet(self):
        
        query = {
            'user': {
                'firstName':self.firstname,
                'lastName':self.lastname,
                'email': self.email
            }
        }
        self.response = requests.put(
            url = SHEETY_ENDPOINT,
            headers = AUTHORIZATION_HEADER,
            json= query
            )
        self.response.status_code
        print(self.response.text)