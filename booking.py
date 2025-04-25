from ticket import Ticket


class Booking:
    def __init__(self):
        self.bookings = []

    def ticket_book(self, passenger, flight):
        booking = Ticket(passenger, flight)
        self.bookings.append(booking)
        return f"A foglalás sikeresen megtörtént! Ár: {flight.price} Ft"

    def ticket_cancel(self, passenger, flight):
        for booking in self.bookings:
            if booking.passenger == passenger and booking.flight.id == flight:
                self.bookings.remove(booking)
                return "A foglalás sikeresen lemondva!"
        return "Nem található foglalás a megadott adatokkal."

    def bookings_list(self):
        if not self.bookings:
            return "Nincsenek aktuális foglalások."
        return [booking.ticket_information() for booking in self.bookings]
