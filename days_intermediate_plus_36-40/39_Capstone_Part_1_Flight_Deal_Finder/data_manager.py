import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ['SHEETY_PRICES_ENDPOINT']
SHEETY_USERS_ENDPOINT = os.environ['SHEETY_USERS_ENDPOINT']

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data
