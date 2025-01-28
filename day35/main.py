import requests
import config

parameteres = {
    "lat": config.MY_LAT,
    "lon": config.MY_LONG,
    "appid": config.API_KEY,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(config.ENDPOINT, params=parameteres)
response.raise_for_status()

data = response.json()
cloud_codes = [cloud["weather"][0]["id"] for cloud in data["list"]]
for cloud_id in cloud_codes:
    if cloud_id < 700:
        print("take an umbrella")
