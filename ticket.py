class Ticket:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight

    def __str__(self):
        return (
            f"Utas: {self.passenger}\n"
            f"Járat: {self.flight.id}\n"
            f"Úticél: {self.flight.destination}\n"
            f"Indulás: {self.flight.departure_time}\n"
            f"Érkezés: {self.flight.arrival_time}\n"
            f"Menetidő: {self.flight.duration}\n"
            f"Jegyár: {self.flight.price} Ft"
        )

    def ticket_information(self):
        return {
            "passenger": self.passenger,
            "flight_id": self.flight.id,
            "destination": self.flight.destination,
            "departure_time": self.flight.departure_time,
            "arrival_time": self.flight.arrival_time,
            "duration": self.flight.duration,
            "price": self.flight.price,
        }
