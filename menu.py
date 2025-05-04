from utilities import clear_screen

MENU_ITEMS_MAIN = {1: "Járatok", 2: "Foglalás", 3: "Lemondás", 4: "Járataim", 9: "Kilépés"}


def menu_main_print():
    for key, value in MENU_ITEMS_MAIN.items():
        if key == 9:
            print(f"\n{key} - {value}")
        else:
            print(f"{key} - {value}")


def get_valid_name():
    while True:
        name = input("Kérem adja meg a nevét: ").strip()
        if name and name.replace(" ", "").isalpha():
            return name
        else:
            print("\033[1A\033[K\033[1A\033[K\033[1A")
            print("Hibás név! Csak betűket és szóközt tartalmazhat.")


def get_valid_name_from_list(passenger_list):
    while True:
        name = input("Kérem adja meg az utas nevét: ").strip()
        if name in passenger_list:
            return name
        else:
            print("\033[1A\033[K\033[1A\033[K\033[1A")
            print("Hibás utas név! Kérem, válasszon a listában szereplő utasok közül.")


def get_valid_flight_id(flights_list):
    while True:
        flight_id = input("Kérem adja meg a járat azonosítóját: ").strip()
        if flight_id in flights_list:
            return flight_id
        else:
            print("\033[1A\033[K\033[1A\033[K\033[1A")
            print("Hibás járat azonosító! Kérem, válasszon a listában szereplő járatok közül.")


def get_valid_confirmation():
    while True:
        confirmation = input("Biztosan végrehajtja ezt a műveletet? (Igen/Nem): ").strip().lower()
        if confirmation in ["igen", "nem"]:
            return confirmation
        else:
            print("\033[1A\033[K\033[1A\033[K\033[1A\033[K\033[1A\033[K\033[2B\033[1A")
            print("Érvénytelen válasz! Csak 'Igen' vagy 'Nem' érték fogadható el.")


def menu_sub_print(menu_selected, booking_system, airline) -> None:
    if menu_selected == 1:  # SHOW FLIGHTS
        clear_screen()
        print("### JÁRATOK ###\n")

        for flight in airline.flight_id():
            flight_info = flight.flight_information()
            print("-" * 30)
            print(f"Járat azonosító: {flight_info['id']}")
            print(f"Úticél: {flight_info['destination']}")
            print(f"Indulás: {flight_info['departure_time']}")
            print(f"Érkezés: {flight_info['arrival_time']}")
            print(f"Menetidő: {flight_info['duration']}")
            print(f"Jegyár: {flight_info['price']} Ft")
            print("-" * 30, "\n")

        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")

    elif menu_selected == 2:  # BOOK FLIGHT
        clear_screen()
        name = ""
        while name == "":
            print("### FOGLALÁS ###\n")
            name = get_valid_name()
            if name != "":
                clear_screen()
                print("### FOGLALÁS ###\n")
                break

        # Az airline.flight_id() a járatok objektumait adja vissza
        flights_list = [flight.id for flight in airline.flight_id()]

        while True:
            print("\nElérhető járatok listája:\n")
            for flight in airline.flight_id():
                flight_info = flight.flight_information()
                print("-" * 30)
                print(f"Járat azonosító: {flight_info['id']}")
                print(f"Úticél: {flight_info['destination']}")
                print(f"Indulás: {flight_info['departure_time']}")
                print(f"Érkezés: {flight_info['arrival_time']}")
                print(f"Menetidő: {flight_info['duration']}")
                print(f"Jegyár: {flight_info['price']} Ft")
                print("-" * 30, "\n")

            print("\n")
            flight_id = get_valid_flight_id(flights_list)
            if flight_id in flights_list:
                break
            print("A megadott járat nem szerepel a listán. Kérem, adjon meg érvényes járatot.")

        flight = next((f for f in airline.flight_id() if f.id == flight_id), None)
        if flight:
            confirmation = get_valid_confirmation()
            if confirmation == "igen":
                clear_screen()
                print(booking_system.ticket_book(name, flight))
            else:
                clear_screen()
                print("Nem történt foglalás.")

        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")

    elif menu_selected == 3:  # CANCEL FLIGHT
        clear_screen()
        print("### LEMONDÁS ###\n")

        passenger_list = []
        for booking in booking_system.bookings:
            if booking.passenger not in passenger_list:
                passenger_list.append(booking.passenger)

        if passenger_list:
            print("Elérhető utasok:\n")
            for passenger in passenger_list:
                print(f"- {passenger}")
        else:
            print("Nincsenek foglalások a rendszerben.")
            input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")
            return

        print("\n")
        name = get_valid_name_from_list(passenger_list)
        booked_flights = [booking.flight for booking in booking_system.bookings if booking.passenger == name]

        if not booked_flights:
            print("A megadott név nem szerepel az utaslistán.")
        else:
            print("\nFoglalásai:\n")
            for flight in booked_flights:
                print("-" * 30)
                print(
                    f" Utas: {name}\n"
                    f" Járat: {flight.id}\n"
                    f" Úticél: {flight.destination}\n"
                    f" Indulás: {flight.departure_time}\n"
                    f" Érkezés: {flight.arrival_time}\n"
                    f" Menetidő: {flight.duration}\n"
                    f" Jegyár: {flight.price} Ft"
                )
                print("-" * 30, "\n")

            print("\n")
            flight_id = get_valid_flight_id([f.id for f in booked_flights])
            confirmation = get_valid_confirmation()
            if confirmation == "igen":
                clear_screen()
                print(booking_system.ticket_cancel(name, flight_id))
            else:
                clear_screen()
                print("Nem történt lemondás.")

        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")

    elif menu_selected == 4:  # SHOW "MY" TICKETS
        clear_screen()
        print("### JÁRATAIM ###\n")

        passenger_list = []
        for booking in booking_system.bookings:
            if booking.passenger not in passenger_list:
                passenger_list.append(booking.passenger)

        if passenger_list:
            print("Elérhető utasok:\n")
            for passenger in passenger_list:
                print(f"- {passenger}")
            print("\n")
        else:
            print("Nincsenek foglalások a rendszerben.")
            input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")
            return

        name = get_valid_name_from_list(passenger_list)
        print("\033[2A\033[K\033[1B")
        bookings = [booking.ticket_information() for booking in booking_system.bookings if booking.passenger == name]

        if not bookings:
            print("Nincsenek foglalásai.")
        else:
            print("\nFoglalásai:\n")
            for flight in bookings:
                print("-" * 30)
                print(
                    f" Utas: {flight['passenger']}\n"
                    f" Járat: {flight['flight_id']}\n"
                    f" Úticél: {flight['destination']}\n"
                    f" Indulás: {flight['departure_time']}\n"
                    f" Érkezés: {flight['arrival_time']}\n"
                    f" Menetidő: {flight['duration']}\n"
                    f" Jegyár: {flight['price']} Ft"
                )
                print("-" * 30, "\n")

        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")

    elif menu_selected == 9:
        clear_screen()
        print("A program bezárult.")
        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")
        exit()


def menu_main(booking_system, airline):
    while True:
        clear_screen()
        menu_main_print()
        try:
            menu_selected = int(input("\nVálasszon egy menüpontot: "))
            if menu_selected in MENU_ITEMS_MAIN:
                menu_sub_print(menu_selected, booking_system, airline)
            else:
                print("Érvénytelen beviteli érték.")
        except ValueError:
            print("Hibás beviteli érték! Csak egész számot adjon meg!")
