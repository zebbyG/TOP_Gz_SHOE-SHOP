from colorama import init, Fore, Style

init()


def display_pradas():
    """
    :return: Prada shoes
    """
    pradas = ["Prada cloudBust", "Prada Linea Rossa", "Prada cup",
              "Prada Punta Ala high", "Women Prada Pegasus", "Prada loafers"]
    for p in pradas:
        print(p)

    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE:(~check spelling~)\n" + Style.RESET_ALL)
        type_shoe = input()
        print("")
        if type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if type_shoe == pradas[0]:
        print(pradas[0], "retails at" + Fore.BLUE + " $37.80\033[0m")

    elif type_shoe == pradas[1]:
        print(pradas[1], "retails at" + Fore.BLUE + " $40.50\033[0m")

    elif type_shoe == pradas[2]:
        print(pradas[2], "retails at" + Fore.BLUE + " $44.00\033[0m")

    elif type_shoe == pradas[3]:
        print(pradas[3], "retails at" + Fore.BLUE + " $49.20\033[0m")

    elif type_shoe == pradas[4]:
        print(pradas[4], "retails at" + Fore.BLUE + " $46.00\033[0m")

    elif type_shoe == pradas[5]:
        print(pradas[5], "retails at" + Fore.BLUE + " $38.85\033[0m")

    else:
        pass
