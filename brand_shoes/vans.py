from colorama import init, Fore, Style
from credentials import var_global

init()


def display_vans() -> str:
    """
    :return: vans shoes
    """
    vans = ["Vans old skool", "Vans Men Sk8-Hi", "Vans Slip-on", "vans Authentic", "Vans Women high cut",
            "Vans Sk8-mid"]
    for v in vans:
        print(v)

    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if var_global.type_shoe == vans[0]:
        print(vans[0], "retails at" + Fore.BLUE + " $15.00\033[0m")

    elif var_global.type_shoe == vans[1]:
        print(vans[1], "retails at" + Fore.BLUE + " $21.39\033[0m")

    elif var_global.type_shoe == vans[2]:
        print(vans[2], "retails at" + Fore.BLUE + " $22.90\033[0m")

    elif var_global.type_shoe == vans[3]:
        print(vans[3], "retails at" + Fore.BLUE + " $17.00\033[0m")

    elif var_global.type_shoe == vans[4]:
        print(vans[4], "retails at" + Fore.BLUE + " $22.30\033[0m")

    elif var_global.type_shoe == vans[5]:
        print(vans[5], "retails at" + Fore.BLUE + " $27.25\033[0m")

    else:
        pass
