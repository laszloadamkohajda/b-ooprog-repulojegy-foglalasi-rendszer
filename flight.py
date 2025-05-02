from abc import ABC, abstractmethod


class Flight(ABC):
    def __init__(self, id, destination, price, departure_time, arrival_time, duration):
        self.id = id
        self.destination = destination
        self.price = price
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.duration = duration

    @abstractmethod
    def flight_information():
        pass


class DomesticFlight(Flight):
    def __init__(self, id, destination, price, departure_time, arrival_time, duration):
        super().__init__(id, destination, price, departure_time, arrival_time, duration)

    def flight_information(self):
        return {
            "type": "BELFÖLDI JÁRAT",
            "id": self.id,
            "destination": self.destination,
            "price": self.price,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "duration": self.duration,
        }


class InternationalFlight(Flight):
    def __init__(self, id, destination, price, departure_time, arrival_time, duration):
        super().__init__(id, destination, price, departure_time, arrival_time, duration)

    def flight_information(self):
        return {
            "type": "NEMZETKÖZI JÁRAT",
            "id": self.id,
            "destination": self.destination,
            "price": self.price,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "duration": self.duration,
        }
