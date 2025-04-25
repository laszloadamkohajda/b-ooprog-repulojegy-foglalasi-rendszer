from abc import ABC, abstractmethod


class Flight(ABC):
    def __init__(self, id, destination, price, time_from, time_to, time_duration):
        self.id = id
        self.destination = destination
        self.price = price
        self.time_from = time_from
        self.time_to = time_to
        self.time_duration = time_duration

    @abstractmethod
    def flight_information():
        pass


class DomesticFlight(Flight):
    def __init__(self, id, destination, price, time_from, time_to, time_duration):
        super().__init__(id, destination, price, time_from, time_to, time_duration)

    def flight_information(self):
        return f"\n BELFÖLDI JÁRAT\n Azonosító: {self.id}\n Úticél: {self.destination}\n Indulás: {self.time_from}\n Érkezés: {self.time_to}\n Menetidő: {self.time_duration}\n Jegyár: {self.price} Ft\n"


class InternationalFlight(Flight):
    def __init__(self, id, destination, price, time_from, time_to, time_duration):
        super().__init__(id, destination, price, time_from, time_to, time_duration)

    def flight_information(self):
        return f"\n NEMZETKÖZI JÁRAT\n Azonosító: {self.id}\n Úticél: {self.destination}\n Indulás: {self.time_from}\n Érkezés: {self.time_to}\n Menetidő: {self.time_duration}\n Jegyár: {self.price} Ft\n"
