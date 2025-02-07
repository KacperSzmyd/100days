import config
from datetime import datetime
import requests

APP_ID = config.APP_ID
API_KEY = config.API_KEY
AUTH = config.AUTH
ENDPOINT = "/v2/natural/exercise"
NLP_URL = "https://trackapi.nutritionix.com"

SHEET_URL = "https://api.sheety.co/9f8ff7ef22fd3e1ddd27095d3583d209/workoutTrackerWithPython/arkusz1"


nlp_headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}

exercise = input("What type of excercise you did, and for how long?: ")

nlp_parameteres = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 97,
    "height_cm": 190,
    "age": 26,
}

nlp_response = requests.post(
    url=f"{NLP_URL}{ENDPOINT}", headers=nlp_headers, json=nlp_parameteres
)
nlp_response.raise_for_status()
data = nlp_response.json()["exercises"]
print(data)
now = datetime.now()

for exercise in data:
    exercise_data = {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M"),
        "exercise": exercise["name"],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }

    sheet_parameteres = {
        "arkusz1": exercise_data,
    }

    sheety_response = requests.post(url=SHEET_URL, json=sheet_parameteres, headers=AUTH)
    sheety_response.raise_for_status()
    print(sheet_parameteres)
