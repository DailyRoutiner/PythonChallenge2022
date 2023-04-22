import requests
from flight_data import FlightData
import pprint


TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "use API"
tequila_headers = {
    "Content-Type": "application/json",
    "apikey": TEQUILA_API_KEY
}
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city):
        tequila_params = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=tequila_params, headers=tequila_headers)
        tequila_data = response.json()
        city_code = tequila_data["locations"][0]["code"]
        # print(city_code)
        return city_code


    def get_lowest_price(self, origin_city_code, destination_city_code, date_from, date_to):

        tequila_code_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "curr": "CAD"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=tequila_code_params, headers=tequila_headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
            pprint.pprint(data)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_airport_code=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_city_code=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_arrival"].split("T")[0]
        )
        print(f"{flight_data.destination_city} : ${flight_data.price} ")
        return flight_data


