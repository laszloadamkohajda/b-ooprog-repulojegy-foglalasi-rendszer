from utilities import clear_screen

MENU_ITEMS_MAIN = [[1, "Járatok"], [2, "Foglalás"], [3, "Lemondás"], [4, "Járataim"], [9, "Kilépés"]]


def menu_main_print() -> None:
    clear_screen()
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
        input()

    elif menu_selected == 2:  # BOOK FLIGHT
        clear_screen()
        print("### FOGLALÁSOK ###\n")
        for booking_item in booking_system.bookings_list():
            print(f"{booking_item}")
        input()

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
            name = input("\nAdja meg az utas nevét: ")
            clear_screen()

            if name not in passenger_list:
                print("A név nem szerepel az utaslistán. Kérlek, adj meg egy érvényes nevet.")
            else:
                break

        clear_screen()
        print("### JÁRATAIM ###\n")
        for booking_item in booking_system.bookings_list():
            if name in booking_item:
                print(f"{booking_item}")

        id = input("Adja meg a lemondani kívánt járatot: ")
        clear_screen()

        verification = input(
            f"Biztosan le szeretné mondani a {name} nevére és {id} járatra szóló foglalást? (Igen/Nem): "
        )
        if verification.lower() == "igen":
            clear_screen()
            print(booking_system.ticket_cancel(name, id))
        else:
            print("Nem történt lemondás.")

        input()

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
            name = input("\nAdja meg az utas nevét: ")
            clear_screen()

            if name not in passenger_list:
                print("A név nem szerepel az utaslistán. Kérlek, adj meg egy érvényes nevet.")
            else:
                break

        clear_screen()
        print("### JÁRATAIM ###\n")
        for booking_item in booking_system.bookings_list():
            if name in booking_item:
                print(f"{booking_item}")
        input()

    elif menu_selected == 9:
        clear_screen()
        print("A program bezárult.\n")


def menu_main(booking_system, airline) -> None:
    menu_selected = 0

    while menu_selected != 9:
        menu_main_print()
        menu_selected = int(input("\nVálasszon egy menüpontot: "))
        menu_sub_print(menu_selected, booking_system, airline)
