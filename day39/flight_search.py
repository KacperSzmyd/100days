import requests
import datetime


class FlightSearch:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.flight_search_endpoint = (
            "https://test.api.amadeus.com/v2/shopping/flight-offers"
        )
        self.token = self.get_token()

    def get_token(self) -> str:
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }
        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers=header,
            data=body,
        )
        response.raise_for_status()
        return response.json()["access_token"]

    def get_IATA(self, city) -> str:
        url = "https://test.api.amadeus.com/v1/reference-data/locations"
        token_header = {
            "Authorization": f"Bearer {self.token}",
        }
        parameters = {"subType": "CITY", "keyword": f"{city}", "view": "LIGHT"}
        response = requests.get(url=url, headers=token_header, params=parameters)
        response.raise_for_status()
        data = response.json()["data"][0]
        return data["iataCode"]

    def get_offers(self, destination, origin_location="BER", adults=2):
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

        token_header = {
            "Authorization": f"Bearer {self.token}",
        }
        parameteres = {
            "originLocationCode": origin_location,
            "destinationLocationCode": destination,
            "departureDate": tomorrow.strftime("%Y-%m-%d"),
            "adults": adults,
            "nonStop": "true",
            "currencyCode": "EUR",
        }
        response = requests.get(
            url=self.flight_search_endpoint, headers=token_header, params=parameteres
        )
        response.raise_for_status()
        return response.json()["data"]

    def get_prices(self, destination, origin_location="BER", adults=2):
        offers = self.get_offers(destination, origin_location, adults)
        prices = []
        for offer in offers:
            prices.append(offer["price"]["base"])
        return prices
