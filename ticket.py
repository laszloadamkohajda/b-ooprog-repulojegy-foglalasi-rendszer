class Ticket:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight

    def ticket_information(self):
        return f"Foglalás: Utas neve: {self.passenger}, Járat: {self.flight.id}, Célállomás: {self.flight.destination}, Jegyár: {self.flight.price} Ft"
