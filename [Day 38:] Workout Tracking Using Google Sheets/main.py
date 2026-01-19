import requests
import datetime as dt
import os

from dotenv import load_dotenv
load_dotenv()

GENDER = 'male'
WEIGHT_KG = 78
HEIGHT_CM = 157
AGE = 39

APP_ID = os.getenv('APP_ID')
APP_APIKEY = os.getenv('APP_APIKEY')

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = os.getenv('SHEET_ENDPOINT')


exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_APIKEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


# ---------------------------------------- 
# Creating a new row on the sheet
# ----------------------------------------

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

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

# ----------------------------------------
# Bearer Token Authentication
# ----------------------------------------

bearer_headers = {
"Authorization": f"Bearer {BEARER_TOKEN}"
}
sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)
    
print(sheet_response.text)