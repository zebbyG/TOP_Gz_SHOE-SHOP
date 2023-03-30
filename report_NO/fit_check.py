from colorama import init, Fore, Style
import time
from credentials import exit_app, var_global
from brand_shoes import brands, display_conditions
from report_NO import brand_choose, order_shoes

init()


def check_fit():
    """
    check if user found a shoe/would want to place an order
    """
    while True:
        var_global.report = input(
            Fore.LIGHTMAGENTA_EX + "\nDid you find your best fit: (yes[y]~~no[n])\n\033[0m").lower().strip()
        if var_global.report:
            break
        else:
            print(Fore.RED + "required field\033[0m")
    if var_global.report == "no" or var_global.report == "n":
        while True:
            try:
                check_other = {
                    "1": "Back to main menu",
                    "2": "exit"
                    }
                time.sleep(0.6)
                print(Fore.YELLOW + f"1: {check_other['1']}\n" + Fore.RED + f"2: {check_other['2']}\n" +
                      Style.RESET_ALL)
                check_other = int(input().strip())
                if check_other < 1 or check_other > 2:
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "invalid choice" + Style.RESET_ALL)
        if check_other == 1:
            brands.print_brands()
            brand_choose.choose_brand()
            display_conditions.print_shoes()
            check_fit()
            order_shoes.place_order()
        elif check_other == 2:
            exit_app.exit_app()

    if var_global.report == 'yes' or var_global.report == 'y':
        while True:
            order = input(
                Fore.LIGHTMAGENTA_EX + "Do you want to place an order:(yes[y]~~no[n])\n\033[0m").lower().strip()
            if order:
                break
            else:
                print(Fore.RED + "required field\033[0m")

        if order == 'yes' or order == 'y':
            order_shoes.place_order()
        elif order == "no" or order == "n":

            while True:
                try:
                    choice = {
                        "1": "Back to main menu",
                        "2": "Exit"
                    }
                    time.sleep(0.6)
                    print(Fore.YELLOW + f"1: {choice['1']}\n" + Fore.RED + f"2: {choice['2']}"
                          + Style.RESET_ALL)
                    continue_exit = int(input().strip())
                    if continue_exit < 1 or continue_exit > 2:
                        raise ValueError
                    break  # exit the loop if the input is valid
                except ValueError:
                    print(Fore.RED + "Invalid choice" + Style.RESET_ALL)

            if continue_exit == 1:
                brands.print_brands()
                brand_choose.choose_brand()
                display_conditions.print_shoes()
                check_fit()
                order_shoes.place_order()
            elif continue_exit == 2:
                exit_app.exit_app()
