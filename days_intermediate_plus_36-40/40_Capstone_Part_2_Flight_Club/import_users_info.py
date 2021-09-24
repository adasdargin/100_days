import os
import requests

SHEETY_USERS_ENDPOINT = os.environ['SHEETY_USERS_ENDPOINT']

print(f"Welcome to ADA Flight Club\nWe find the best flight deals and email you.")
first_name = input("What's your first name?\n")
last_name = input("What's your last name?\n")
email = input("What's your email?\n")
confirm_email = input("Type your email again.\n")
if email == confirm_email:
    print("You're in the club")

    user_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(url=SHEETY_USERS_ENDPOINT, json=user_data)
    print(response.text)