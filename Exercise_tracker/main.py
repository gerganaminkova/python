import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

APP_ID = os.environ.get("x-app-id")
APP_KEY = os.environ.get("x-app-key")
TOKEN = os.environ.get("x-app-token")

GENDER = "female"
WEIGHT_KG = 47
HEIGHT_CM = 169
AGE = 21

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/35f9ad57a15593169f427e941d335677/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, headers=headers, json=parameters)
result = response.json()


now_time = datetime.now().strftime("%d/%m/%Y")
today_day = datetime.now().strftime("%A")

bearer_header={
    "Authorization": f"Bearer {TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_day,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response= requests.post(sheet_endpoint, json=sheet_inputs,headers=bearer_header)
    print(sheet_response.text)
