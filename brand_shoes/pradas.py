from colorama import init, Fore, Style
from credentials import var_global

init()


def display_pradas():
    """
    print Prada shoes and price
    """
    var_global.pradas = {
        "Prada cloudBust": "$378",
        "Prada Linea Rossa": "$405",
        "Prada cup": "$231",
        "Prada Punta Ala high": "$112",
        "Women Prada Pegasus": "$107",
        "Prada loafers": "$251"
    }

    for p in var_global.pradas.keys():
        print(p)

    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE:(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if var_global.type_shoe == "Prada cloudBust":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.pradas[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Prada Linea Rossa":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.pradas[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Prada cup":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.pradas[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Prada Punta Ala high":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.pradas[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Women Prada Pegasus":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.pradas[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Prada loafers":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.pradas[var_global.type_shoe]}\033[0m")

    else:
        print(Fore.RED + "shoe not found recheck and enter available shoes\n" + Style.RESET_ALL)
        display_pradas()
