from colorama import init, Fore, Style
from credentials import var_global

init()


def display_jordans():
    """
    :return:
    """
    jordans = ["Air jordan 1", "Jordan j11 Retro Concord", "Mens air jordan 9 retro", "Air jordan 3",
               "Women jordan air 1 low", "Air jordan v"]
    for j in jordans:
        print(j)
    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE:(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if var_global.type_shoe == jordans[0]:
        print(f"{jordans[0]} retails at" + Fore.BLUE + "$25.00\033[0m")

    elif var_global.type_shoe == jordans[1]:
        print(jordans[1], "retails at" + Fore.BLUE + " $21.00\033[0m")

    elif var_global.type_shoe == jordans[2]:
        print(jordans[2], "retails at" + Fore.BLUE + " $27.00\033[0m")

    elif var_global.type_shoe == jordans[3]:
        print(jordans[3], "retails at" + Fore.BLUE + " $19.00\033[0m")

    elif var_global.type_shoe == jordans[4]:
        print(jordans[4], "retails at" + Fore.BLUE + " $31.00\033[0m")

    elif var_global.type_shoe == jordans[5]:
        print(jordans[5], "retails at" + Fore.BLUE + " $29.00\033[0m")

    else:
        pass
