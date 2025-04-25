from menu import menu_main
from airline import Airline
from flight import DomesticFlight, InternationalFlight
from booking import Booking


def flights_init(airline):
    airline.flight_append(DomesticFlight("ML-D-1", "Debrecen", 19490, "06:15", "06:45", "00:30"))
    airline.flight_append(InternationalFlight("ML-N-2", "London", 46890, "09:35", "11:25", "01:50"))
    airline.flight_append(InternationalFlight("ML-N-3", "Bécs", 35290, "14:05", "15:15", "01:10"))

    return airline


def bookings_init(airline):
    booking_system = Booking()
    booking_system.ticket_book("Gipsz Jakab", airline.flights[0])
    booking_system.ticket_book("Kemp Elek", airline.flights[1])
    booking_system.ticket_book("Kukor Ica", airline.flights[0])
    booking_system.ticket_book("Akciós Áron", airline.flights[0])
    booking_system.ticket_book("Lassú Anett", airline.flights[1])
    booking_system.ticket_book("Minta Márton", airline.flights[2])

    return booking_system


def main() -> None:

    airline = flights_init(Airline("MALÉV", "ML"))
    booking_system = bookings_init(airline)

    input()
    menu_main(booking_system, airline)


if __name__ == "__main__":
    main()
