from menu import menu_main
from airline import Airline
from flight import DomesticFlight, InternationalFlight
from booking import Booking


def main() -> None:

    airline1 = Airline("Wizz Air", "W")
    dom_flight1 = DomesticFlight("W12345", "Debrecen", 21490)
    int_flight1 = InternationalFlight("W54321", "London", 43890)

    airline1.flight_append(dom_flight1)
    airline1.flight_append(int_flight1)

    booking_system = Booking()
    print(booking_system.ticket_book("Gipsz Jakab", int_flight1))
    print(booking_system.ticket_book("Kemp Elek", dom_flight1))
    print(booking_system.bookings_list())
    print(booking_system.ticket_cancel("Gipsz Jakab", "W54321"))
    print(booking_system.bookings_list())

    input()
    menu_main()


if __name__ == "__main__":
    main()
