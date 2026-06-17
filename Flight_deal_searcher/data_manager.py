import os
import requests
from dotenv import load_dotenv
from twilio.rest.api.v2010.account.recording.add_on_result.payload import data


class DataManager:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('SHEETY_TOKEN')
        self.flight_endpoint = os.getenv("SHEETY_FLIGHTS_ENDPOINT")
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")

        self.destination_data = {}

    def get_flight_data(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(self.flight_endpoint, headers=headers)
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
            url=f"{self.flight_endpoint}/{row_id}",
            headers=headers,
            json=body
        )
        response.raise_for_status()
        print(f"Row {row_id} has been changed to {new_price}")

    def get_customer_email(self):
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url=self.users_endpoint, headers=headers)
        data = response.json()

        return data["users"]



