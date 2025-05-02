from utilities import clear_screen

MENU_ITEMS_MAIN = [[1, "Járatok"], [2, "Foglalás"], [3, "Lemondás"], [4, "Járataim"], [9, "Kilépés"]]


def menu_main_print() -> None:
    for menu_item in MENU_ITEMS_MAIN:
        if menu_item[0] == 9:
            print(f"\n{menu_item[0]} - {menu_item[1]}")
        else:
            print(f"{menu_item[0]} - {menu_item[1]}")


def menu_sub_print(menu_selected, booking_system, airline) -> None:
    if menu_selected == 1:  # SHOW FLIGHTS
        clear_screen()
        print("### JÁRATOK ###\n")
        for flight_item in airline.flight_information():
            print(f"{flight_item}")

        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")

    elif menu_selected == 2:  # BOOK FLIGHT
        clear_screen()

        flights_list = []
        for flight_item in airline.flight_id():
            flights_list.append(flight_item.id)

        while True:
            while True:
                print("### FOGLALÁS ###\n")
                name = input("Kérem adja meg a nevét: ").strip()
                if name and name.replace(" ", "").isalpha():
                    clear_screen()
                    print("### FOGLALÁS ###\n")
                    break
                else:
                    clear_screen()
                    print("A megadott név helytelen. Kérem, adjon meg egy érvényes nevet.\n")

            while True:
                print(f"Az ön neve: {name}\n")
                print("Elérhető járatok listája:\n")
                for flight_item in airline.flight_information():
                    print(f"{flight_item}")

                id = input("\nKérem adja meg a járatot: ")
                clear_screen()
                if id in flights_list:
                    clear_screen()
                    break
                else:
                    print("### FOGLALÁS ###\n")
                    print("A megadott járat nem szerepel az járatlistán. Kérem, adjon meg egy érvényes járatot.\n")

            print("### FOGLALÁS ###\n")
            for flight_item in airline.flight_id():
                if flight_item.id == id:
                    print(flight_item.flight_information())

            verification = input(f"Biztosan le szeretné foglalni {name} névre a(z) {id} járatot? (Igen/Nem): ")
            if verification.lower() == "igen":
                clear_screen()
                print(booking_system.ticket_book(name, flight_item))
            else:
                clear_screen()
                print("Nem történt foglalás.")

            input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")
            break

    elif menu_selected == 3:  # CANCEL FLIGHT
        clear_screen()
        print("### LEMONDÁS ###")

        passenger_list = []
        for booking_item in booking_system.bookings:
            passenger_list.append(booking_item.passenger)

        while True:
            print("\nElérhető utasok listája:")
            for passenger_name in passenger_list:
                print(f" - {passenger_name}")
            name = input("\nKérem adja meg az utas nevét: ")
            clear_screen()

            if name not in passenger_list:
                print("A megadott név nem szerepel az utaslistán. Kérem, adjon meg egy érvényes nevet.")
            else:
                break

        clear_screen()
        while True:
            print("### JÁRATOK ###\n")
            for booking_item in booking_system.bookings_list():
                if name in booking_item:
                    print(f"{booking_item}")

            id = input("Kérem adja meg a lemondani kívánt járatot: ")
            if len(id) == 6 and id in booking_item:
                break
            else:
                clear_screen()
                print("A megadott járat nem szerepel a megadott utasnál. Kérem, adjon meg egy érvényes járatot.\n")

        verification = input(
            f"Biztosan le szeretné mondani a(z) {name} nevére és {id} járatra szóló foglalást? (Igen/Nem): "
        )
        if verification.lower() == "igen":
            clear_screen()
            print(booking_system.ticket_cancel(name, id))
        else:
            clear_screen()
            print("Nem történt lemondás.")

        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")

    elif menu_selected == 4:  # SHOW "MY" TICKETS
        clear_screen()
        print("### JÁRATAIM ###")

        passenger_list = []
        for booking_item in booking_system.bookings:
            passenger_list.append(booking_item.passenger)

        while True:
            print("\nElérhető utasok listája:")
            for passenger_name in passenger_list:
                print(f" - {passenger_name}")
            name = input("\nKérem adja meg az utas nevét: ")
            clear_screen()

            if name not in passenger_list:
                print("A megadott név nem szerepel az utaslistán. Kérem, adjon meg egy érvényes nevet.")
            else:
                break

        clear_screen()
        print("### JÁRATAIM ###\n")
        for booking_item in booking_system.bookings_list():
            if name in booking_item:
                print(f"{booking_item}")

        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")

    elif menu_selected == 9:
        clear_screen()
        print("A program bezárult.")
        input("\nA folytatáshoz kérem nyomjon meg egy billentyűt...")
        exit()


def menu_main(booking_system, airline) -> None:
    menu_selected = 0

    menu_items_id = []
    for i in MENU_ITEMS_MAIN:
        menu_items_id.append(i[0])

    clear_screen()
    while menu_selected != 9:
        while True:
            menu_main_print()
            menu_selected = input("\nVálasszon egy menüpontot: ")
            if menu_selected.isdigit() and int(menu_selected) in menu_items_id:
                clear_screen()
                break
            else:
                clear_screen()
                print("Kérem csak egész számot adjon meg!\n")

        menu_sub_print(int(menu_selected), booking_system, airline)
        clear_screen()
