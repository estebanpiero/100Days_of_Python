# Day 40: Capstone Part 2 - Flight Club

## Project: Flight Club - Automated Deal Notifications

### Description
The completion of the Flight Deal Finder project, now with user registration and automated email/SMS notifications. Users can sign up to receive alerts about cheap flights to destinations they're interested in. This capstone project brings together everything learned: APIs, data management, automation, and communication.

### What I Learned
- User management system
- Email notifications with formatted HTML
- SMS notifications via Twilio
- Customer database management
- Automated alert systems
- Final project integration
- Complete application workflow
- Production-ready code practices

### How to Run
```bash
python3 main.py
```

### New Features (Part 2)
- User registration system
- Email alert notifications
- SMS alert notifications (optional)
- Multi-user support
- Customer database in Google Sheets
- Formatted email templates
- Automated daily checks

### Project Structure (Complete)
```
Day40_FlightClub/
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py ← NEW
└── customer_acquisition.py ← NEW
```

### New Classes

#### NotificationManager
```python
import smtplib
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.my_email = os.environ.get("MY_EMAIL")
        self.my_password = os.environ.get("EMAIL_PASSWORD")
        self.twilio_account_sid = os.environ.get("TWILIO_SID")
        self.twilio_auth_token = os.environ.get("TWILIO_TOKEN")
        self.twilio_number = os.environ.get("TWILIO_NUMBER")
        self.client = Client(self.twilio_account_sid,
                           self.twilio_auth_token)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)
            for email in emails:
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}"
                )

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.twilio_number,
            to="YOUR_PHONE_NUMBER"
        )
        print(message.sid)
```

#### CustomerAcquisition
```python
class CustomerAcquisition:
    def __init__(self):
        self.endpoint = SHEETY_USERS_ENDPOINT

    def add_user(self, first_name, last_name, email):
        new_row = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(self.endpoint, json=new_row)
        return response.text
```

### User Registration Flow
```python
from customer_acquisition import CustomerAcquisition

customer_manager = CustomerAcquisition()

print("Welcome to Flight Club!")
print("We find the best flight deals and email them to you.")

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email1 = input("What is your email? ")
email2 = input("Type your email again: ")

if email1 == email2:
    customer_manager.add_user(first_name, last_name, email1)
    print("You're in the club!")
else:
    print("Emails don't match. Please try again.")
```

### Google Sheets Structure

#### Sheet 1: Prices (Destinations)
| City | IATA Code | Lowest Price |
|------|-----------|--------------|
| Paris | CDG | 100 |
| Berlin | BER | 80 |

#### Sheet 2: Users (NEW)
| First Name | Last Name | Email |
|------------|-----------|-------|
| John | Doe | john@email.com |
| Jane | Smith | jane@email.com |

### Enhanced Main Logic
```python
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Get data
sheet_data = data_manager.get_destination_data()
customer_data = data_manager.get_customer_emails()

# Update IATA codes if missing
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row["city"])

data_manager.update_destination_codes()

# Search flights
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )

    if flight and flight.price < destination["lowestPrice"]:
        message = (f"Low price alert! Only £{flight.price} "
                  f"to fly from {flight.origin_city} "
                  f"to {flight.destination_city}, "
                  f"from {flight.out_date} to {flight.return_date}.")

        # Send to all users
        notification_manager.send_emails(customer_data, message)
        # Optional: Send SMS
        # notification_manager.send_sms(message)
```

### Email Template (Enhanced)
```python
message = f"""Subject:Low Price Alert!

Only £{price} to fly from {origin} to {destination}

Departure: {out_date}
Return: {return_date}

Book now: {booking_link}

Happy travels!
Flight Club
"""
```

### Automation Setup

#### Using PythonAnywhere (Free Tier)
1. Upload code to PythonAnywhere
2. Set environment variables
3. Create scheduled task (daily at 9 AM)
4. Script runs automatically every day

#### Using Cron (Linux/Mac)
```bash
# Edit crontab
crontab -e

# Run every day at 9 AM
0 9 * * * /usr/bin/python3 /path/to/main.py
```

### Environment Variables Needed
```bash
export TEQUILA_API_KEY="your_key"
export SHEETY_PRICES_ENDPOINT="your_endpoint"
export SHEETY_USERS_ENDPOINT="your_endpoint"
export MY_EMAIL="your_email"
export EMAIL_PASSWORD="your_password"
export TWILIO_SID="your_sid"
export TWILIO_TOKEN="your_token"
export TWILIO_NUMBER="your_number"
```

### Complete Features
✓ Flight price monitoring
✓ Multiple destinations
✓ User registration
✓ Email notifications
✓ SMS notifications (optional)
✓ Google Sheets database
✓ Automated daily checks
✓ Price comparison
✓ IATA code management

### Key Concepts
- **Full-Stack Application**: Complete user journey
- **User Management**: Registration and storage
- **Notification Systems**: Multiple channels (email/SMS)
- **Automation**: Scheduled daily execution
- **Data Management**: Multiple sheets coordination
- **Error Handling**: Robust error checking
- **Security**: Environment variables
- **Production Ready**: Deployable application

### Learning Focus
Capstone project demonstrating mastery of Python, APIs, automation, data management, and building complete production-ready applications. Combines all skills from the course.

### Congratulations!
This completes Day 40 and demonstrates the ability to build sophisticated, real-world applications using Python!
