import requests
from datetime import datetime


MY_LAT = 54.695777
MY_LNG = 25.254427

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise_hour)
print(sunset_hour)

time_now = datetime.now()
print(time_now.hour)
