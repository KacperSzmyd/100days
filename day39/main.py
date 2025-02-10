# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
import config
from time import sleep
from pprint import pprint


URL = "https://api.sheety.co/9f8ff7ef22fd3e1ddd27095d3583d209/flightDeals/arkusz1"
AUTH = config.AUTH

dm = DataManager(URL, AUTH)
fs = FlightSearch(config.AMADEUS_API_KEY, config.AMADEUS_API_SECRET)

sheet_data = dm.get_data()


for data in sheet_data:
    city = data["city"]
    if data["iataCode"] == "":
        dm.set_IATA_code(fs.get_IATA(city), city)

cheap_flights = []
for data in sheet_data:
    lowest_price = data["lowestPrice"]
    iata_code = data["iataCode"]
    offers = fs.get_offers(iata_code)
    sleep(5)
    for offer in offers:
        price = float(offer["price"]["base"])
        if price < lowest_price and price > 0:
            pprint(offer)
            fd = FlightData(
                price,
                offer["price"]["grandTotal"],
                offer["itineraries"][0]["segments"][0]["departure"]["at"],
                offer["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
            )
            cheap_flights.append(fd)
            print(fd)
            print("-" * 20)
