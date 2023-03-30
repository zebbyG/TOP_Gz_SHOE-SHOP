import time

from colorama import init, Fore, Style
# import time
from credentials import exit_app, var_global
from brand_shoes import brands, display_conditions
from report_NO import brand_choose, order_shoes

init()


def check_fit():
    while True:
        var_global.report = input(
            Fore.LIGHTMAGENTA_EX + "\nDid you find your best fit: (yes[y]~~no[n])\n\033[0m").lower().strip()
        if var_global.report:
            break
        else:
            print(Fore.RED + "Cannot be empty\033[0m")
    if var_global.report == "no" or var_global.report == "n":
        print(Fore.BLUE + "would you like to check shoes in other brands[y]/[n]" + Style.RESET_ALL)
        check_other = input().lower().strip()
        if check_other:
            brands.print_brands()
            brand_choose.choose_brand()
            display_conditions.print_shoes()
            check_fit()
        elif check_other == "y" or check_other == "yes":
            brands.print_brands()
            brand_choose.choose_brand()
            display_conditions.print_shoes()
            check_fit()

        else:
            print(Fore.BLUE + f"Sorry {var_global.new_user_name} \033[0m.\n" +
                  Fore.YELLOW + "You can come check later to find your best fit :). Welcome!!\n\033[0m")
            time.sleep(1)
            print(Fore.GREEN + "\nTHANKS FOR VISITING TOP_G'z ONLINE SHOE SHOP :)\033[0m"
                  + Fore.BLUE + "\nHope to see you again soon\033[0m")
            exit_app.exit_app()

    if var_global.report == 'yes' or var_global.report == 'y':
        while True:
            order = input(
                Fore.LIGHTMAGENTA_EX + "Do you want to place an order:(yes[y]~~no[n])\n\033[0m").lower().strip()
            if order:
                break
            else:
                print(Fore.RED + "Cannot be empty\033[0m")

        if order == 'yes' or order == 'y':
            order_shoes.place_order()
        else:
            print(Fore.GREEN + "\nTHANKS FOR VISITING TOP_G'z ONLINE SHOE SHOP :)\033[0m"
                  + Fore.BLUE + "\nHope to see you again soon\033[0m")
            exit_app.exit_app()
