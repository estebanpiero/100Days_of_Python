# This script checks the current location of the International Space Station (ISS)

import requests
from datetime import datetime, timedelta
import smtplib
import os

# ---------- Email Configuration ----------

FROM_EMAIL = os.getenv("FROM_EMAIL")  # Your email address
TO_EMAIL = os.getenv("TO_EMAIL")      # Recipient email address
PASSWORD = os.getenv("EMAIL_PASSWORD")  # Your email password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


# ---------- User's location ----------

MY_LAT = 41.087  # Your latitude
MY_LONG = -74.131  # Your longitude

my_possition = (MY_LAT, MY_LONG)

# ---------- Function to check if ISS is overhead ----------

def is_iss_overhead(iss_lat, iss_long, my_lat, my_long):
    """Check if the ISS is within +5 or -5 degrees of the user's location."""
    if (my_lat - 5) <= iss_lat <= (my_lat + 5) and (my_long - 5) <= iss_long <= (my_long + 5):
        return True
    return False

# ---------- Get the current position of the ISS ----------

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

iss_data = response.json()
iss_latitude = float(iss_data['iss_position']['latitude'])
iss_longitude = float(iss_data['iss_position']['longitude'])
iss_position = (iss_latitude, iss_longitude)

print(f"ISS Position: {iss_position}")
print(f"My Position: {my_possition}")

# ---------- Check for the SunSet and Sunrise times ----------

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

sunset_sunrise_response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
sunset_sunrise_response.raise_for_status()
data = sunset_sunrise_response.json()

sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0]) # Get hour of sunrise
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])  # Get hour of sunset

print(f"Sunrise: {sunrise}, Sunset: {sunset}")


# ---------- Check if it's currently night time ----------

time_now = datetime.now()

if sunrise <= time_now.hour <= sunset:
    print("It's daytime.")
else:
    print("It's nighttime.")
    if is_iss_overhead(iss_latitude, iss_longitude, MY_LAT, MY_LONG):
        print("The ISS is overhead! Look up!")
        # Send email notification
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(FROM_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
            )


