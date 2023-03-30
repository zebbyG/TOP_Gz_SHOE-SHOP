from colorama import init, Fore, Style
from credentials import var_global
init()


def choose_brand():
    """
    choose a brand
    """
    while True:
        try:
            var_global.pick = int(input(Fore.LIGHTMAGENTA_EX + "CHOOSE BRAND:(~enter number~)\n"
                                        + Style.RESET_ALL))
            print("")
            if var_global.pick < 1 or var_global.pick > 5:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + f"Recheck and enter available brands\033[0m")
