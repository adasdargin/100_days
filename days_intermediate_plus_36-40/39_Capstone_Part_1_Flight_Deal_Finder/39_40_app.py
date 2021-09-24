# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "VNO"

data_mananager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_mananager.get_sheet_data()

if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row['city'])
    data_mananager.update_destination_codes()
    data_mananager.destination_data = sheet_data

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        tomorrow,
        six_months_from_now
    )

    if flight is None:
        continue

    if flight.price < destination['lowestPrice']:

        users = data_mananager.get_customer_emails()
        emails = [row['email'] for row in users]

        message = f"Low price alert! Only €{flight.price} " \
                f"to fly from {flight.origin_city}-{flight.origin_airport} " \
                f"to {flight.destination_city}-{flight.destination_airport}, " \
                f"from {flight.departure_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city} City."

        # notification_manager.send_message(message)

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.departure_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)

