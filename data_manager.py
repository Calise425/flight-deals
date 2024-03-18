import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    """This class talks to the Google sheet"""
    def __init__(self):
        self.api_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.sheety_auth = os.getenv("SHEETY_AUTH")
        self.header = {
            "Authorization": self.sheety_auth
        }

    def get_sheet(self):
        """Fetches the sheet with flight destination information"""
        response = requests.get(url=self.api_endpoint, headers=self.header)
        data = response.json()
        return data['prices']

    def put_sheet(self, object_id, body):
        response = requests.put(url=f"{self.api_endpoint}/{object_id}", headers=self.header, json=body)
        print(response.text)
