#new_list = [new_item for item in list]
#new_dic = {new_key:new_value for (key,value) in dic.items()}
#new_dic = {new_key:new_value for (index,row) in df.iterrows()}

import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_USERNAME = os.getenv('SHEETY_USERNAME')
SHEETY_PROJECT_NAME = os.getenv('SHEETY_PROJECT_NAME')
SHEETY_SHEET = 'flightPrices'
SHEETY_ENDPOINT = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET}'

AUTHORIZATION_HEADER = {
    'Authorization': f'Bearer {os.getenv("SHEETY_BEARER_TOKEN")}'
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        
    def fligt_information(self):
        self.response = requests.get(SHEETY_ENDPOINT,headers = AUTHORIZATION_HEADER)
        self.response.status_code
        self.destination_data =  self.response.json()['flightPrices']
        return self.destination_data
        
    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                'flightPrice': {
                    'iataCode' : city['iataCode']
                    }
                }   
            sheet_update = requests.put(
                url = f'{SHEETY_ENDPOINT}/{city["id"]}',
                headers = AUTHORIZATION_HEADER,
                json = new_data
            )

            #print(sheet_update.status_code)
            #print(sheet_update.text)
        
        
        
        
