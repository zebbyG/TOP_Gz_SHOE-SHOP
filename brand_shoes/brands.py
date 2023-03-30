from credentials import var_global
from colorama import init, Fore, Style

init()


def print_brands():
    """
    print the brands available in the shop
    """
    var_global.brand = {
        "1": "Jordan",
        "2": "Nikes",
        "3": "Yeezys",
        "4": "Vans",
        "5": "Pradas"
    }
    print("-" * 50)
    print(Fore.BLUE + "Welcome to our catalog. You can place an order anytime" + Style.RESET_ALL)
    print("-" * 50)
    show_brands = input(Fore.LIGHTMAGENTA_EX + "Press enter to see available brands\033[0m")
    if show_brands:
        pass
    else:
        pass
    print("We have:")
    print(f"1: {var_global.brand['1']}\n2: {var_global.brand['2']}\n3: {var_global.brand['3']}\n"
          f"4: {var_global.brand['4']}\n5: {var_global.brand['5']}")
