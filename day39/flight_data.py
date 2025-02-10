class FlightData:
    def __init__(self, price, grand_total, date, iata):
        self.price = price
        self.grand_total = grand_total
        self.date = (date,)
        self.iata_code = iata

    def __str__(self):
        return f"{self.iata_code}\n{self.date}\n{self.price}\n{self.grand_total}"
