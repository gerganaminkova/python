import os
import requests
from dotenv import load_dotenv


class DataManager:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('SHEETY_TOKEN')
        self.endpoint = "https://api.sheety.co/35f9ad57a15593169f427e941d335677/flights/flights"
        self.destination_data = {}

    def get_flight_data(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(self.endpoint, headers=headers)
        data = response.json()

        self.destination_data = data["flights"]
        return self.destination_data

    def change_the_price(self,row_id,new_price):
        body={
            "flight": {
                "lowestPrice":new_price,
            }
        }
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.put(
            url=f"{self.endpoint}/{row_id}",
            headers=headers,
            json=body
        )
        response.raise_for_status()
        print(f"Row {row_id} has been changed to {new_price}")




