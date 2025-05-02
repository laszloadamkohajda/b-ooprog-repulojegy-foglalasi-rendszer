class Airline:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.flights = []

    def flight_append(self, flights):
        self.flights.append(flights)

    def flight_information(self):
        if not self.flights:
            return ["Nincsenek aktuális járatok."]

        flight_info_list = []
        for flight in self.flights:
            flight_info_list.append(flight.flight_information())
        return flight_info_list

    def flight_id(self):
        return self.flights
