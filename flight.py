from abc import ABC, abstractmethod


class Flight(ABC):
    def __init__(self, id, destination, price):
        self.id = id
        self.destination = destination
        self.price = price

    @abstractmethod
    def flight_information():
        pass


class DomesticFlight(Flight):
    def __init__(self, id, destination, price):
        super().__init__(id, destination, price)

    def flight_information(self):
        return f"Belföldi járat - Azonosító: {self.id}, Úticél: {self.destination}, Jegyár: {self.price} Ft"


class InternationalFlight(Flight):
    def __init__(self, id, destination, price):
        super().__init__(id, destination, price)

    def flight_information(self):
        return f"Nemzetközi járat - Azonosító: {self.id}, Úticél: {self.destination}, Jegyár: {self.price} Ft"
