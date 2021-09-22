import requests
from datetime import datetime
import os

USERNAME = "adaspix"
TOKEN = os.environ["PIXELA_TOKEN"]
GRAPH_ID = "graph1"

# 1 create user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)                  #{"message":"Success. Let's visit https://pixe.la/@adasdargin , it is your profile page!","isSuccess":true}


# 2 create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)              #{"message":"Success.","isSuccess":true}
#https://pixe.la/v1/users/adaspix/graphs/graph1.html

# 3 post pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ")
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)


# 4 update pixel
date_to_modify = "20210917"
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_modify}"
pixel_update_data = {"quantity": "3.00"}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)


# 5 delete pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_modify}"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)

