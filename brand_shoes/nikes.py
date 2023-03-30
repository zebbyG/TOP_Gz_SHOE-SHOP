from colorama import init, Fore, Style
from credentials import var_global

init()


def display_nikes():
    """
    :return: nike shoes
    """
    nikes = ["Airmax 95", "Air max 270Men", "Air-Force-1", "Nike Air Huarache", "Women Nike High Top", "nike dunk low"]
    for n in nikes:
        print(n)
    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE:(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if var_global.type_shoe == nikes[0]:
        print(nikes[0], "retails at" + Fore.BLUE + " $27.50\033[0m")

    elif var_global.type_shoe == nikes[1]:
        print(nikes[1], "retails at" + Fore.BLUE + " $26.00\033[0m")

    elif var_global.type_shoe == nikes[2]:
        print(nikes[2], "retails at" + Fore.BLUE + " $31.25\033[0m")

    elif var_global.type_shoe == nikes[3]:
        print(nikes[3], "retails at" + Fore.BLUE + " $33.00\033[0m")

    elif var_global.type_shoe == nikes[4]:
        print(nikes[4], "retails at" + Fore.BLUE + " $34.50\033[0m")

    elif var_global.type_shoe == nikes[5]:
        print(nikes[5], "retails at" + Fore.BLUE + " $94.90\033[0m")

    else:
        pass
