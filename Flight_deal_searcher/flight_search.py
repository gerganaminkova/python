import os
import requests
from dotenv import load_dotenv

class FlightSearch:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("SERP_API_KEY")
        self.endpoint = "https://serpapi.com/search"

    def check_flight(self,departure_id,arrival_id,outbound_date,return_date):
        flight_params = {
            "engine": "google_flights",
            "departure_id": departure_id,
            "arrival_id": arrival_id,
            "outbound_date": outbound_date,
            "return_date": return_date,
            "currency": "EUR",
            "hl": "en",
            "api_key": os.getenv("SERP_API_KEY")

        }
        response = requests.get(self.endpoint, params=flight_params)

        flight_info = response.json()
        return flight_info



