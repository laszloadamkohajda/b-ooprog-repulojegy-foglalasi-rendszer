class Ticket:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight

    def __str__(self):
        return (
            f"Utas: {self.passenger}\n"
            f"Járat: {self.flight.id}\n"
            f"Úticél: {self.flight.destination}\n"
            f"Indulás: {self.flight.time_from}\n"
            f"Érkezés: {self.flight.time_to}\n"
            f"Menetidő: {self.flight.time_duration}\n"
            f"Jegyár: {self.flight.price} Ft"
        )

    def ticket_information(self):
        return str(self)
