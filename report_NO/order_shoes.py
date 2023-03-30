from colorama import init, Fore, Style
import time
import datetime
from credentials import exit_app, var_global
from brand_shoes import brands, display_conditions
from report_NO import brand_choose, fit_check

init()


def place_order():
    """
    To place an order for user
    """
    while True:
        # PROMPT LOCATION
        try:
            print(Fore.LIGHTMAGENTA_EX + "Enter your location\n" + Style.RESET_ALL)
            location = input()
            if not location:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Not a valid location" + Style.RESET_ALL)

    while True:
        # PROMPT NUMBER OF PAIRS FOR YOUR ORDER
        """
        while loop to make sure you enter a choice
        """
        try:
            print(Fore.LIGHTMAGENTA_EX + f"\nHow many pairs of {var_global.type_shoe} do you want\n[enter-number]"
                  + Style.RESET_ALL)
            var_global.order_amount = int(input().strip())
            if var_global.order_amount < 1 or type(var_global.order_amount) != int:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + f"\nInvalid input enter a valid number\n")

    while True:
        try:
            print(Fore.LIGHTMAGENTA_EX + "choose 1 to check out" + Style.RESET_ALL)
            choice = {
                "1": "CHECK OUT",
                "2": "Back to main menu",
                "3": "Exit"
            }
            time.sleep(0.6)
            print(Fore.GREEN + f"1: {choice['1']}\n" + Fore.YELLOW + f"2: {choice['2']}\n"
                  + Fore.RED + f"3: {choice['3']}" + Style.RESET_ALL)
            continue_exit = int(input().strip())
            if continue_exit < 1 or continue_exit > 3:
                raise ValueError
            break  # exit the loop if the input is valid
        except ValueError:
            print(Fore.RED + "Invalid input enter a valid number" + Style.RESET_ALL)

    if continue_exit == 1:
        pass
    elif continue_exit == 2:
        brands.print_brands()
        brand_choose.choose_brand()
        display_conditions.print_shoes()
        fit_check.check_fit()
        place_order()
    elif continue_exit == 3:
        exit_app.exit_app()

    print(Fore.LIGHTBLUE_EX + "placing your order...")
    time.sleep(3)
    order = {
            "name": var_global.new_user_name,
            "location": location,
            "shoe_type": var_global.type_shoe,
            "number_of_pairs": str(var_global.order_amount),
        }
    print(Fore.YELLOW + "loading order details..." + Style.RESET_ALL)
    time.sleep(4)
    for key, value in order.items():
        print(key + ": " + Fore.LIGHTMAGENTA_EX + str(value) + Style.RESET_ALL)

    print(Fore.YELLOW + "confirming your order...")
    time.sleep(3)

    z = datetime.datetime.now()
    print(Fore.BLUE + f"{var_global.new_user_name}\033[0m" +
          Fore.GREEN + f" your order for {var_global.order_amount} pair[s] of {var_global.type_shoe} shoe[s]"
                       f" has been successfully placed at\033[0m",
          z.strftime("%Y %b %d %A %H:%M:%S"))
    print(Fore.LIGHTMAGENTA_EX + "\nWe will contact you for more information on your order.\033[0m")
    time.sleep(1)
    print(Fore.GREEN + "\nTHANKS FOR VISITING TOP_G'z ONLINE SHOE SHOP :)\033[0m"
          + Fore.BLUE + "\nHope to see you again soon\033[0m")

    exit_app.exit_app()
