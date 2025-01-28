import requests

MY_LAT = 50.0614300
MY_LONG = 19.9365800
API_KEY = "7b48fa56a84556d5c16bdaece3db9b95"
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameteres = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric",
    "lang": "pl",
    "cnt": 4,
}

response = requests.get(OMW_ENDPOINT, params=parameteres)
response.raise_for_status()

data = response.json()


def will_be_raining(weather_data):
    rainfall_data = [cloud["weather"][0]["id"] for cloud in data["list"]]
    for cloud_id in rainfall_data:
        if cloud_id <= 700:
            print("bring the umbrela")


will_be_raining(data)


