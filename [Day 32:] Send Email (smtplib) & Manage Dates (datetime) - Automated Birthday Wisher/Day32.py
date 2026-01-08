# Sending emails using smtplib

import smtplib
import datetime as dt

my_email = 'myemail@gmail.com' # Replace with your actual email
my_password = '---- ---- ---- ----' # Replace with your actual password or app password
to_email = 'toemail@gmail.com' # Replace with recipient's email
'''
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    
    connection.sendmail(
        from_addr=my_email,
        to_addrs='to_email',
        msg='Subject:Hello\n\nThis is the body of the email.'
    )
'''

# Managing dates using datetime

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
print(f"Year: {year}, Month: {month}, Day: {day}, Weekday: {weekday}")

date_of_birth = dt.datetime(year=1995, month=8, day=15)
print(f"Date of Birth: {date_of_birth}")

