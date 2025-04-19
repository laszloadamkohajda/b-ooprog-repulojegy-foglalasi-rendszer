MENU_ITEMS_MAIN = [[1, "Járatok"], [2, "Foglalás"], [3, "Lemondás"], [4, "Járataim"], [9, "Kilépés"]]


def menu_main() -> None:
    for menu_item in MENU_ITEMS_MAIN:
        if menu_item[0] == 9:
            print(f"\n{menu_item[0]} - {menu_item[1]}")
        else:
            print(f"{menu_item[0]} - {menu_item[1]}")
