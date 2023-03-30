from colorama import init, Fore, Style
from credentials import var_global

init()


def display_nikes():
    """
    print nike shoes and price
    """
    var_global.nikes = {
        "Airmax 95": "$275",
        "Air max 270Men": "$260",
        "Air-Force-1": "$312",
        "Nike Air Huarache": "$330",
        "Women Nike High Top": "$345",
        "nike dunk low": "$118"
    }

    for n in var_global.nikes.keys():
        print(n)
    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE:(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if var_global.type_shoe == "Airmax 95":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.nikes[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Air max 270Men":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.nikes[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Air-Force-1":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.nikes[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Nike Air Huarache":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.nikes[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Women Nike High Top":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.nikes[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "nike dunk low":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.nikes[var_global.type_shoe]}\033[0m")

    else:
        print(Fore.RED + "shoe not found recheck and enter available shoes\n" + Style.RESET_ALL)
        display_nikes()
