from colorama import init, Fore, Style
from credentials import var_global

init()


def display_jordans():
    """
    print jordan shoes and price
    """
    var_global.jordans = {
        "Air jordan 1": "$130",
        "Jordan j11 Retro Concord": "$97",
        "Mens air jordan 9 retro": "$139",
        "Air jordan 3": "$81",
        "Women jordan air 1 low": "$152",
        "Air jordan v": "$146"
    }
    for j in var_global.jordans.keys():
        print(j)
    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE:(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "required field\033[0m")

    if var_global.type_shoe == "Air jordan 1":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.jordans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Jordan j11 Retro Concord":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.jordans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Mens air jordan 9 retro":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.jordans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Air jordan 3":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.jordans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Women jordan air 1 low":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f"{var_global.jordans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Air jordan v":
        print(f"{var_global.type_shoe} retails at " + Fore.BLUE + f"{var_global.jordans[var_global.type_shoe]}\033[0m")

    else:
        print(Fore.RED + "shoe not found recheck and enter available shoes\n" + Style.RESET_ALL)
        display_jordans()
