import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean",
}
# response = requests.get("https://opentdb.com/api.php", params=parameters)
response = requests.get("https://opentdb.com/api.php?amount=10&category=25&type=boolean")
response.raise_for_status()

data = response.json()

question_data = data["results"]
