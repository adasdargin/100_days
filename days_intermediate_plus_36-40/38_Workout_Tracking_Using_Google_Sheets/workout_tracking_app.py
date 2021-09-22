import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 75.0
HEIGHT_CM = 175.00
AGE = 38

NUTRI_API_ID = os.environ['NUTRI_API_ID']
NUTRI_API_KEY = os.environ['NUTRI_API_KEY']
WORKOUTS_SHEETY_API = os.environ['WORKOUTS_SHEETY_API']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = f"https://api.sheety.co/{WORKOUTS_SHEETY_API}/adWorkoutsTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRI_API_ID,
    "x-app-key": NUTRI_API_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

################### Step 4 ######################
USERNAME = "adasdargin"
PASSWORD = os.environ['SHEETY_PASS']

sheet_response = requests.get(url=sheet_endpoint, auth=(USERNAME, PASSWORD))
print(sheet_response.text)

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
now_time = today.strftime("%X")

exercises = result["exercises"]
for ex_data in exercises:
    sheet_inputs = {
        "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": ex_data['name'].title(),
                "duration": ex_data["duration_min"],
                "calories": ex_data["nf_calories"]
            }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))

    print(sheet_response.text)