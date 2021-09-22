import requests
from datetime import datetime
import smtplib
import time
import os

my_email = os.environ["EMAIL_NAME"]
password = os.environ["EMAIL_PASS"]

MY_LAT = 54.695777
MY_LNG = 25.254427


# ---------------------------- ISS ------------------------------- #
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True
    return False


# ---------------------------- SUN ------------------------------- #
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 3

    time_now = datetime.now()

    if sunrise <= time_now.hour <= sunset:
        return False
    return True


# ---------------------------- PROGRAM ------------------------------- #
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="adas.d@icloud.com",
                                msg="Subject:Look up\n\nInternational Space Station is above you in the sky.")
