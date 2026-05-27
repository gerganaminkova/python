import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
NUMBER = os.environ.get("NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")
API_KEY = os.environ.get("API_KEY")
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_parameters = {
    "lat" : 42.70,
    "lon" : 23.32,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(ENDPOINT,params=weather_parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for forcast in weather_data["list"]:
    time = forcast["dt"]

    condition_code = forcast["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="Get an umbrella it will wain today ☂️🌧️",
        from_=NUMBER,
        to=MY_NUMBER,
    )

    print(message.body)


print(message.status)



