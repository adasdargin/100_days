import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()      # {'timestamp': 1621952752, 'message': 'success', 'iss_position': {'longitude': '174.5141', 'latitude': '0.0697'}}

longitude = response.json()["iss_position"]["longitude"]    # 174.5141
latitude = response.json()["iss_position"]["latitude"]      # 0.0697

iss_position_tuple = (longitude, latitude)
print(iss_position_tuple)