import smtplib
import os

my_email = os.environ["EMAIL_NAME"]
password = os.environ["EMAIL_PASS"]

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="adas.d@icloud.com",
                        msg="Subject:Hello2\n\nThis is the body of my email")