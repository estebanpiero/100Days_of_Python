import requests
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_APIKEY = os.getenv('APP_APIKEY')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

GENDER = 'male'
WEIGHT_KG = 70
HEIGHT_CM = 170
AGE = 36

NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com'
EXERCISE_ENDPOINT = '/v2/natural/exercise'

exercise_text = input('What workout did you do today?: ')

HEADERS = {
    'x-app-id':APP_ID,
    'x-app-key':APP_APIKEY
}

PARAMS = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(url=f'{NUTRITIONIX_ENDPOINT}{EXERCISE_ENDPOINT}',headers=HEADERS,json=PARAMS)
print(response.status_code)
result = response.json()


#---------------------------------------------------Sheety API--------------------------------------------------------------------#

#USERNAME = 'tottiflix'
USERNAME = os.getenv('USERNAME')
PROJECT_NAME = os.getenv('PROJECT_NAME')
SHEET = os.getenv('SHEET')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


AUTHORIZATION_HEADER = {
    'Authorization': BEARER_TOKEN
}

# SHEETY_ENPOINT = 'https://api.sheety.co/78516c1e802e09608ef62469f95d576f/myWorkoutsTracking/workouts'
SHEETY_ENPOINT = f'https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET}'


request_sheety = requests.post(SHEETY_ENPOINT,headers=AUTHORIZATION_HEADER,json=sheet_inputs)
print(request_sheety.status_code)
print(request_sheety.text)