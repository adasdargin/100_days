import os
from twilio.rest import Client
import smtplib

TWILO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_NUMBER = "+19102188536"
MY_NUM = os.environ['MY_NUM']

MY_EMAIL = os.environ["EMAIL_NAME"]
MY_PASSWORD = os.environ["EMAIL_PASS"]

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUM
        )

        print(message.status)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject: New Low Price Alert! \n\n{message}\n{google_flight_link}".encode('utf-8')
                                    )