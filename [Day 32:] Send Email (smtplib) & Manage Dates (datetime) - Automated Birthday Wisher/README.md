# Day 32: Send Email (smtplib) & Manage Dates (datetime) - Automated Birthday Wisher

## Project: Automated Birthday Wisher

### Description
An automated program that sends birthday emails to friends and family. The program checks daily if anyone has a birthday, selects a random birthday letter template, personalizes it, and sends it via email automatically.

### What I Learned
- Sending emails with Python (`smtplib`)
- Working with dates and times (`datetime`)
- Reading CSV data
- String formatting and replacement
- Automating tasks
- Working with email templates
- Environment variables for security

### How to Run
```bash
python3 main.py
```

### Features
- Automatic daily birthday checking
- Random birthday letter selection
- Personalized email messages
- CSV-based birthday database
- SMTP email sending
- Template-based messages

### Key Libraries

#### datetime Module
```python
import datetime as dt

# Current date
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()  # Monday=0

# Create specific date
birthday = dt.datetime(year=1995, month=12, day=15)
```

#### smtplib Module (Email)
```python
import smtplib

my_email = "your@email.com"
password = "yourpassword"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # Secure connection
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="recipient@email.com",
        msg="Subject:Hello\n\nThis is the body"
    )
```

### How It Works
1. Check today's date
2. Read birthdays from CSV
3. Check if anyone has birthday today
4. If yes:
   - Select random letter template
   - Replace [NAME] with person's name
   - Send email
5. Run daily (can be automated with task scheduler)

### CSV Format (birthdays.csv)
```csv
name,email,year,month,day
John Doe,john@email.com,1990,5,15
Jane Smith,jane@email.com,1985,12,25
```

### Letter Templates
```
letter_templates/letter_1.txt:
Dear [NAME],

Happy birthday! Wishing you an amazing day
filled with joy and happiness.

Best wishes!
```

### Implementation Pattern
```python
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "your@email.com"
MY_PASSWORD = "yourpassword"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row
                  for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",
                                    birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
```

### Key Concepts
- **Automation**: Running tasks without manual intervention
- **Email Protocols**: SMTP for sending mail
- **Date Handling**: Comparing dates
- **Dictionary Comprehension**: Creating lookup dictionaries
- **Template Files**: Reusable message formats
- **String Replacement**: Personalizing templates

### Gmail Setup Notes
For Gmail, you may need to:
1. Enable "Less secure app access" OR
2. Use App Password (recommended)
3. Use correct SMTP server and port

### SMTP Servers
- Gmail: `smtp.gmail.com`
- Yahoo: `smtp.mail.yahoo.com`
- Outlook: `smtp-mail.outlook.com`

### Security Best Practice
```python
import os

MY_EMAIL = os.environ.get("EMAIL")
MY_PASSWORD = os.environ.get("PASSWORD")
```

### Automation
Set up with cron (Linux/Mac) or Task Scheduler (Windows) to run daily.

### Learning Focus
Automating real-world tasks with email and date handling - practical skills for productivity and automation scripts.
