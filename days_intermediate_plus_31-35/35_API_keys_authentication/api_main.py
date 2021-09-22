import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ["OWM_API_KEY"]

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_number = "+19102188536"

weather_params = {
    "lat": 40.839981,
    "lon": 14.252540,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)

# for i in range(12):
#     hourly_id = data["hourly"][i]["weather"][0]["id"]
#     if hourly_id < 700:
#         print("Bring an umbrella")
#         break

will_rain = False
weather_slice = data["hourly"][:12]
print(weather_slice)
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella ☔️",
        from_=twilio_number,
        to=os.environ['MY_NUM']
    )

    print(message.status)