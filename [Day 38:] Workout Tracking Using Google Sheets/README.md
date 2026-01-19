# Day 38: Workout Tracking Using Google Sheets

## Project: Exercise Tracker with Natural Language Processing

### Description
An intelligent exercise tracking system that uses natural language processing (via Nutritionix API) to interpret workout descriptions and automatically logs them to a Google Sheet (via Sheety API). Simply describe your workout in plain English, and the app handles the rest.

### What I Learned
- Natural Language Processing APIs
- Nutritionix API for exercise tracking
- Sheety API for Google Sheets integration
- Bearer token authentication
- POST requests with authentication
- Environment variables for sensitive data
- Combining multiple APIs
- Date and time handling

### How to Run
```bash
python3 main.py
```

### Features
- Natural language workout input
- Automatic exercise recognition
- Calorie calculation
- Duration estimation
- Google Sheets logging
- Timestamp tracking
- Multiple exercises in one input

### APIs Used

#### 1. Nutritionix API (Natural Language Processing)
```python
import requests

NUTRITIONIX_APP_ID = "your_app_id"
NUTRITIONIX_API_KEY = "your_api_key"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

exercise_text = "ran 3 miles and cycled for 30 minutes"

body = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 180,
    "age": 30
}

response = requests.post(exercise_endpoint,
                        json=body,
                        headers=headers)
result = response.json()
```

#### 2. Sheety API (Google Sheets)
```python
SHEETY_ENDPOINT = "https://api.sheety.co/YOUR_SHEET_ENDPOINT"

headers = {
    "Authorization": f"Bearer {YOUR_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(SHEETY_ENDPOINT,
                            json=sheet_inputs,
                            headers=headers)
```

### Nutritionix Response Format
```json
{
    "exercises": [
        {
            "name": "running",
            "duration_min": 20,
            "nf_calories": 150.5,
            "met": 8.0
        },
        {
            "name": "cycling",
            "duration_min": 30,
            "nf_calories": 200.0,
            "met": 6.0
        }
    ]
}
```

### Google Sheet Structure
| Date | Time | Exercise | Duration | Calories |
|------|------|----------|----------|----------|
| 15/12/2023 | 14:30:00 | Running | 20 | 150.5 |
| 15/12/2023 | 14:30:00 | Cycling | 30 | 200.0 |

### Bearer Token Authentication
```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE"
}

# Or
headers = {
    "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"
}
```

### Full Implementation
```python
import requests
from datetime import datetime
import os

# Nutritionix
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 180,
    "age": 30
}

response = requests.post(exercise_endpoint,
                        json=parameters,
                        headers=headers)
result = response.json()

# Sheety
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

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

    sheet_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        headers=sheet_headers
    )

    print(sheet_response.text)
```

### Setting Up Sheety

1. Create Google Sheet with columns: Date, Time, Exercise, Duration, Calories
2. Go to sheety.co
3. Connect your Google Sheet
4. Enable POST requests
5. Set up Bearer Token authentication (recommended)
6. Copy your API endpoint

### Example Inputs
```
"ran 3 miles"
"walked for 45 minutes"
"did 30 minutes of yoga and 20 minutes of strength training"
"cycled 10 kilometers"
"swam for 1 hour"
```

### Key Concepts
- **Natural Language Processing**: AI understanding human language
- **Bearer Tokens**: Secure authentication method
- **Multiple POST Requests**: One to analyze, multiple to log
- **Datetime Formatting**: Creating timestamp strings
- **Environment Variables**: Secure credential storage
- **API Chaining**: Using output from one API as input for another

### Security Best Practices
```python
# Don't hardcode credentials
# BAD:
API_KEY = "12345abcde"

# GOOD:
API_KEY = os.environ.get("API_KEY")
```

### Advanced Features
- Add user stats (weight, height, age) as env variables
- Create weekly summary
- Calculate total calories burned
- Add exercise categories
- Set up automated daily logging reminder

### Learning Focus
Combining NLP with cloud spreadsheets to create an intelligent data entry system - demonstrating how AI APIs can simplify user input and automate data logging.
