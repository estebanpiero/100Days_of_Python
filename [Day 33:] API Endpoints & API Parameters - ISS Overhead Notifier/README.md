# Day 33: API Endpoints & API Parameters - ISS Overhead Notifier

## Project: ISS Overhead Notifier

### Description
An automated program that sends an email notification when the International Space Station (ISS) is overhead at night. Uses real-time ISS position API and sunset/sunrise API to determine optimal viewing conditions.

### What I Learned
- Working with APIs (Application Programming Interfaces)
- Making HTTP requests with `requests` library
- Parsing JSON responses
- API parameters and endpoints
- HTTP status codes
- Working with geographic coordinates
- Combining multiple APIs
- Scheduled task automation

### How to Run
```bash
python3 main.py
```

### Features
- Real-time ISS position tracking
- Sunset/sunrise time calculation
- Location-based detection
- Email notifications
- Runs continuously, checks every 60 seconds

### APIs Used

#### 1. ISS Position API
```python
response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```

#### 2. Sunrise-Sunset API
```python
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json",
                       params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
```

### HTTP Status Codes
```python
response = requests.get(url="http://api.example.com/data")

# Status codes
# 1XX: Informational
# 2XX: Success (200 OK, 201 Created)
# 3XX: Redirection
# 4XX: Client Error (404 Not Found)
# 5XX: Server Error

if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorized.")

# Or use:
response.raise_for_status()  # Raises exception if not 2XX
```

### Logic Flow
1. Get current ISS position
2. Check if ISS is close to your location (within ±5 degrees)
3. Check if it's currently night time
4. If both conditions true: send email notification
5. Wait 60 seconds, repeat

### Full Implementation
```python
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351
MY_LONG = -0.127758
MY_EMAIL = "your@email.com"
MY_PASSWORD = "yourpassword"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5 and
        MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json",
                           params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
            )
```

### Key Concepts
- **APIs**: Accessing external data services
- **HTTP Requests**: GET requests with parameters
- **JSON Parsing**: Extracting data from JSON responses
- **Status Codes**: Handling different response types
- **API Parameters**: Customizing requests
- **Continuous Running**: Infinite loop with sleep
- **Boolean Logic**: Combining multiple conditions

### API Concepts
- **Endpoint**: URL where API can be accessed
- **Parameters**: Data sent to customize request
- **Response**: Data returned from API
- **JSON**: Standard format for API data

### Finding Your Coordinates
Use latlong.net or Google Maps to find your latitude and longitude.

### Error Handling
```python
response = requests.get(url)
response.raise_for_status()  # Raises HTTPError if status not 200
```

### Learning Focus
Introduction to APIs - connecting to external services to access real-time data and build location-aware applications.
