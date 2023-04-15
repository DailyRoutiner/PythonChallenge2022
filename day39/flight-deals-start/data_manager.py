import requests
from pprint import pprint


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    sheety_endpoint = "https://api.sheety.co/7efcfd83d14084ae585651511e041f64/flightDeals/prices"


    response = requests.get(url=sheety_endpoint)
    json_flight = response.json()
    pprint(json_flight)
    sheet_data = json_flight('prices')

    # send json data to main.py




dt = DataManager()