class Ticket:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight

    def ticket_information(self):
        return f"\n UTAS: {self.passenger}\n Járat: {self.flight.id}\n Úticél: {self.flight.destination}\n Indulás: {self.flight.time_from}\n Érkezés: {self.flight.time_to}\n Menetidő: {self.flight.time_duration}\n Jegyár: {self.flight.price} Ft\n"
