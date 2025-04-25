class Airline:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.flights = []

    def flight_append(self, flights):
        self.flights.append(flights)

    def flight_information(self):
        return [flight.flight_information() for flight in self.flights]
