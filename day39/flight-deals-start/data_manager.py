import requests

SHEETY_ENDPOINT = "https://api.sheety.co/7efcfd83d14084ae585651511e041f64/flightDeals/prices"
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        #This class is responsible for talking to the Google Sheet.
        response = requests.get(url=SHEETY_ENDPOINT)
        json_flight = response.json()

        # send json data to main.py
        self.destination_data = json_flight['prices']
        return self.destination_data

    def update_destination_data(self):

        for city in self.destination_data:
            new_data = {
                "price" : {  # 왜 price로 키를 줘야 하지??
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
