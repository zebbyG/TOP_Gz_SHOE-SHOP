from colorama import init, Fore, Style
from credentials import var_global

init()


def display_vans():
    """
    print vans shoes and price
    """
    var_global.vans = {
        "Vans old skool": "$150",
        "Vans Men Sk8-Hi": "213",
        "Vans Slip-on": "$229",
        "vans Authentic": "$160",
        "Vans Women high cut": "$223",
        "Vans Sk8-mid": "$117"
    }
    # vans = ["Vans old skool", "Vans Men Sk8-Hi", "Vans Slip-on", "vans Authentic", "Vans Women high cut",
    #         "Vans Sk8-mid"]
    for v in var_global.vans.keys():
        print(v)

    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if var_global.type_shoe == "Vans old skool":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.vans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Vans Men Sk8-Hi":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.vans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Vans Slip-on":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.vans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "vans Authentic":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.vans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Vans Women high cut":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.vans[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Vans Sk8-mid":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" {var_global.vans[var_global.type_shoe]}\033[0m")

    else:
        print(Fore.RED + f"shoe {var_global.type_shoe} not found recheck and enter available shoes\n" + Style.RESET_ALL)
        display_vans()
