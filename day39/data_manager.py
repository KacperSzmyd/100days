import requests


class DataManager:
    def __init__(self, url, auth):
        self.url = url
        self.auth = auth
        self.city_keys = {_["city"]: _["id"] for _ in self.get_data()}

    def get_data(self) -> list:
        response = requests.get(url=self.url, headers=self.auth)
        response.raise_for_status()
        data = response.json()["arkusz1"]

        return data

    def set_IATA_code(self, code, city):
        city_id = self.city_keys[f"{city.title()}"]
        parameters = {
            "arkusz1": {"iataCode": code},
        }
        response = requests.put(
            url=f"{self.url}/{city_id}", headers=self.auth, json=parameters
        )
        response.raise_for_status()
