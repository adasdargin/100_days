from datetime import datetime
import pandas
import smtplib
from random import randint
import os

my_email = os.environ["EMAIL_NAME"]
password = os.environ["EMAIL_PASS"]

today = datetime.now()
today_tuple = (today.month, today.day)

data_df = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data_df.iterrows()}

if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", birthday_dict[today_tuple]["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{birthday_dict[today_tuple]['email']}",
                            msg=f"Subject: Happy Birthday\n\n{new_letter}")
