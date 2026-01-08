# Automated Birthday Email Service

import smtplib
import datetime as dt   
import pandas as pd
import random

birthdays_file_path = '/home/argento/Documents/Education/100Days_of_Python/[Day 32:] Send Email (smtplib) & Manage Dates (datetime) - Automated Birthday Wisher/Automated Birthday Email Service/'  # CSV file containing birthday data
birthdays_letters_path = '/home/argento/Documents/Education/100Days_of_Python/[Day 32:] Send Email (smtplib) & Manage Dates (datetime) - Automated Birthday Wisher/Automated Birthday Email Service/letter_templates/'  # Folder containing letter templates
# Load birthday data

birthdays_df = pd.read_csv(f'{birthdays_file_path}birthdays.csv')  # Ensure you have a CSV file with 'name', 'email', 'year', 'month', 'day' columns
birthdays_dict = birthdays_df.to_dict(orient='records') 

# Get today's date
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# Email credentials

my_email = 'myemail@gmail.com'  # Replace with your actual email
my_password = '---- ---- ---- ----'  # Replace with your actual password or app password

# Check for birthdays today and send emails

for birthday in birthdays_dict:
    if birthday['month'] == today_month and birthday['day'] == today_day:
        name = birthday['name']
        email = birthday['email']
        
        # Select a random letter template
        
        letter_num = random.randint(1, 3)  # Assuming you have 3 letter templates named letter_1.txt, letter_2.txt, letter_3.txt

        letter_path = f"{birthdays_letters_path}letter_{letter_num}.txt"  # You can randomize this if you have multiple templates
        with open(letter_path, 'r') as letter_file:
            letter_content = letter_file.read()
            personalized_letter = letter_content.replace('[NAME]', name)
        
        # Send the email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f'Subject:Happy Birthday!\n\n{personalized_letter}'
            )