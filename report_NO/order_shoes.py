from colorama import init, Fore, Style
import time
import datetime
from credentials import var_global, exit_app
init()


def place_order():
    """

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
            print(Fore.LIGHTMAGENTA_EX + f"\nHow many pairs of {var_global.type_shoe} do you want\n[enter-number]" + Style.RESET_ALL)
            var_global.order_amount = int(input())
            if var_global.order_amount < 1:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + f"\ncannot order {var_global.order_amount} pairs\n")

    print(Fore.LIGHTBLUE_EX + "placing your order...")
    time.sleep(3)
    order = {
        "name": var_global.new_user_name,
        "location": location,
        "brand": var_global.pick,
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
