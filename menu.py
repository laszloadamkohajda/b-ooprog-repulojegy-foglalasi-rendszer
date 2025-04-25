from utilities import clear_screen

MENU_ITEMS_MAIN = [[1, "Járatok"], [2, "Foglalás"], [3, "Lemondás"], [4, "Járataim"], [9, "Kilépés"]]


def menu_main_print() -> None:
    clear_screen()
    for menu_item in MENU_ITEMS_MAIN:
        if menu_item[0] == 9:
            print(f"\n{menu_item[0]} - {menu_item[1]}")
        else:
            print(f"{menu_item[0]} - {menu_item[1]}")


def menu_sub_print(menu_selected) -> None:
    if menu_selected == 1:
        clear_screen()
        print("Járatok")
        input()
    elif menu_selected == 2:
        clear_screen()
        print("Foglalások")
        input()
    elif menu_selected == 3:
        clear_screen()
        print("Lemondás")
        input()
    elif menu_selected == 4:
        clear_screen()
        print("Járataim")
        input()
    elif menu_selected == 9:
        clear_screen()
        print("A program bezárult.\n")


def menu_main() -> None:
    menu_selected = 0

    while menu_selected != 9:
        menu_main_print()
        menu_selected = int(input("\nVálasszon egy menüpontot: "))
        menu_sub_print(menu_selected)
