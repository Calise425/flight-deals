import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
FLY_FROM = "DEN"
TEQUILA_ENDPOINT = os.getenv("KIWI_ENDPOINT")
API_KEY = os.getenv("KIWI_API_KEY")


class FlightSearch:
    """The class responsible for talking to the Tequila API and searching for flight info"""
    def __init__(self):
        self.headers = {"apikey": API_KEY}

    def get_aita(self, city_name):
        """Takes a city name and returns the city IATA code"""
        search_data = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=self.headers, params=search_data)
        data = response.json()["locations"]
        return data[0]["code"]

    def search_for_flights(self, destination: str):
        """Takes the destination IATA code and searches for the lowest cost flight"""
        tomorrow = datetime.now() + timedelta(days=1)
        six_months_out = datetime.now() + timedelta(days=180)
        search_data = {
            "fly_from": FLY_FROM,
            "fly_to": destination,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months_out.strftime("%d/%m/%Y"),
            "curr": "USD",
            "limit": 5
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", headers=self.headers, params=search_data)
        data = response.json()
        price = data["data"][0]["price"]
        departing_unix = int(data["data"][0]["dTime"])
        departing_date = datetime.fromtimestamp(departing_unix)
        print("City: ", destination, "Departing: ", departing_date, "\nPrice: $", price)
