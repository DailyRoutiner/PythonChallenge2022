import requests
from datetime import datetime


user_endpoint = "https://pixe.la/v1/users"

create_user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=user_endpoint, json=create_user_params)
# print(response.text)


graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": "graph1",
    "name": "Reading Daily",
    "unit": "Page",
    "type": "int",
    "color": "sora"
}

graph_header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)
# print(response.text)

pixel_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2"
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=graph_header)
print(response.text)