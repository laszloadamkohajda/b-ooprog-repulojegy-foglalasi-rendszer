from menu import menu_main
from airline import Airline
from flight import DomesticFlight, InternationalFlight
from booking import Booking


def flights_init(airline):
    airline.flight_append(DomesticFlight("A111", "Debrecen", 19490))
    airline.flight_append(InternationalFlight("A222", "London", 46890))
    airline.flight_append(DomesticFlight("A333", "Budapest", 23290))

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

    airline = flights_init(Airline("Betyár Társaság", "A"))
    booking_system = bookings_init(airline)

    input()
    menu_main(booking_system, airline)


if __name__ == "__main__":
    main()
