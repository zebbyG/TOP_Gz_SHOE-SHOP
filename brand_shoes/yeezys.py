from colorama import init, Fore, Style
from credentials import var_global
init()


def display_yeezys():
    yeezys = ["Yeezy 700", "Yeezy 350s", "Yeezy slides", "Yeezy powerphase",
              "YEEZY 450's", "Yeezy 500 Blush"]
    for y in yeezys:
        print(y)

    while True:
        print(Fore.LIGHTMAGENTA_EX + "CHOOSE SHOE:(~check spelling~)\n" + Style.RESET_ALL)
        var_global.type_shoe = input()
        print("")
        if var_global.type_shoe:
            break
        else:
            print(Fore.RED + "Cannot be empty. Please choose a shoe type\033[0m")

    if var_global.type_shoe == yeezys[0]:
        print(yeezys[0], "retails at" + Fore.BLUE + " $26.00\033[0m")

    elif var_global.type_shoe == yeezys[1]:
        print(yeezys[1], "retails at" + Fore.BLUE + " $39.00\033[0m")

    elif var_global.type_shoe == yeezys[2]:
        print(yeezys[2], "retails at" + Fore.BLUE + " $19.80\033[0m")

    elif var_global.type_shoe == yeezys[3]:
        print(yeezys[3], "retails at" + Fore.BLUE + " $21.85\033[0m")

    elif var_global.type_shoe == yeezys[4]:
        print(yeezys[4], "retails at" + Fore.BLUE + " $18.00\033[0m")

    elif var_global.type_shoe == yeezys[5]:
        print(yeezys[5], "retails at" + Fore.BLUE + " $24.90\033[0m")

    else:
        print(Fore.RED + "shoe not found recheck and enter available shoes" + Style.RESET_ALL)
        display_yeezys()
