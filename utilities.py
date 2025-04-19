import os


def clear_screen():
    # for Windows
    if os.name == "nt":
        _ = os.system("cls")

    # Mac or Linux
    else:
        _ = os.system("clear")
