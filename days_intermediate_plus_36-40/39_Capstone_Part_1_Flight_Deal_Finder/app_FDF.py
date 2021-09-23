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
    print(sheet_data)

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

    try:
        if flight.price < destination['lowestPrice']:
            notification_manager.send_message(
                message=f"Low price alert! Only €{flight.price} to fly from "
                        f"{flight.origin_city}-{flight.origin_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport}, from "
                        f"{flight.departure_date} to {flight.return_date}.")
    except AttributeError:
        pass
