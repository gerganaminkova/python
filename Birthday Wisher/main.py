import smtplib
import datetime as dt
from random import random

MY_EMAIL = "gerganaPythonTest.yahoo.com"
PASSWORD = "python2026"


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL, msg=f"Subject:Monday motivation!\n\n{random_quote}")

