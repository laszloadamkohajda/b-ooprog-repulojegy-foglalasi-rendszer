from utilities import clear_screen

MENU_ITEMS_MAIN = {1: "Járatok", 2: "Foglalás", 3: "Lemondás", 4: "Járataim", 9: "Kilépés"}


def menu_main_print():
    for key, value in MENU_ITEMS_MAIN.items():
        if key == 9:
            print(f"\n{key} - {value}")
        else:
            print(f"{key} - {value}")


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
        print("### FOGLALÁS ###\n")
        name = input("Kérem adja meg a nevét: ").strip()

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

            flight_id = input("\nKérem adja meg a járatot: ").strip()
            if flight_id in flights_list:
                break
            print("A megadott járat nem szerepel a listán. Kérem, adjon meg érvényes járatot.")

        flight = next((f for f in airline.flight_id() if f.id == flight_id), None)
        if flight:
            confirmation = input(f"Biztosan lefoglalja {name} névre a(z) {flight_id} járatot? (Igen/Nem): ").lower()
            if confirmation == "igen":
                print(booking_system.ticket_book(name, flight))
            else:
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

        name = input("\nKérem adja meg az utas nevét: ").strip()
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
                print("-" * 30)

            flight_id = input("\nKérem adja meg a lemondani kívánt járatot: ").strip()
            for i in range(len(booked_flights)):
                if flight_id in booked_flights[i].id:
                    confirmation = input(
                        f"Biztosan lemondja a(z) {name} nevű utas {flight_id} járatát? (Igen/Nem): "
                    ).lower()
                    if confirmation == "igen":
                        print(booking_system.ticket_cancel(name, flight_id))
                    else:
                        print("Nem történt lemondás.")
                else:
                    print("A megadott járat nem szerepel az utasnál.")

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
        else:
            print("Nincsenek foglalások a rendszerben.")
            input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")
            return

        name = input("\nKérem adja meg az utas nevét: ").strip()
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
