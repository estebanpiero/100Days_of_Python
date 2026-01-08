# Send Motivational Quotes via Email

import smtplib
import random
import datetime as dt

filepath = "file_path/"  # Replace with the actual path to your quotes.txt file

# Useing today's date for the email subject

now = dt.datetime.now()
today_date = now.day
today_month = now.month
weekday = now.weekday()

MAIL_FROM = 'mail_from@gmail.com'  # Replace with your email
MAIL_PASSWORD = 'your_app_password'  # Replace with your email password or app password
MAIL_TO = 'mail_to@gmail.com'      # Replace with recipient's email

if weekday == 0:  # Send only on Mondays
    
    # Get a random motivational quote from the file

    with open(f'{filepath}quotes.txt') as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    # Send the quote via email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(
            user=MAIL_FROM,
            password=MAIL_PASSWORD
        )
        connection.sendmail(
            from_addr=MAIL_FROM,
            to_addrs=MAIL_TO,
            msg=f"Subject:Motivational Quote\n\n{random_quote}"
        )