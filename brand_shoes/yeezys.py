from colorama import init, Fore, Style
from credentials import var_global
init()


def display_yeezys():
    """
    print yeezy shoes and price
    """
    var_global.yeezys = {
        "Yeezy 700": "260",
        "Yeezy 350s": "177",
        "Yeezy slides": "93",
        "Yeezy powerphase": "218",
        "YEEZY 450's": "180",
        "Yeezy 500 Blush": "103"
    }

    for y in var_global.yeezys:
        print(y)

    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE:(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if var_global.type_shoe == "Yeezy 700":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" ${var_global.yeezys[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Yeezy 350s":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" ${var_global.yeezys[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Yeezy slides":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" ${var_global.yeezys[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Yeezy powerphase":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" ${var_global.yeezys[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "YEEZY 450's":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" ${var_global.yeezys[var_global.type_shoe]}\033[0m")

    elif var_global.type_shoe == "Yeezy 500 Blush":
        print(f"{var_global.type_shoe} retails at" + Fore.BLUE + f" ${var_global.yeezys[var_global.type_shoe]}\033[0m")

    else:
        print(Fore.RED + f"shoe {var_global.type_shoe} not found recheck and enter available shoes\n" + Style.RESET_ALL)
        display_yeezys()
