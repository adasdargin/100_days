import random
import smtplib
import datetime as dt
import os

MY_EMAIL = os.environ["EMAIL_NAME"]
PASSWORD = os.environ["EMAIL_PASS"]

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as data:
        all_quotes = data.readlines()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="adas.d@icloud.com",
                            msg=f"Subject:Monday motivation letter\n\n{random.choice(all_quotes)}")