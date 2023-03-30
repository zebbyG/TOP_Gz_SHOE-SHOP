from colorama import init, Fore, Style
import time
from credentials import create_account, log_in, exit_app, var_global
from brand_shoes import brands, display_conditions
from report_NO import brand_choose, fit_check
init()

"""
THIS IS THE START OF THE BOT
"""
print("=" * 60)
print("=" * 60)
print(Fore.BLUE + "\tHELLO! WELCOME TO Top G'z ONLINE SHOE SHOP." + Style.RESET_ALL)
print("=" * 60)
print("=" * 60)

"""
This is to help user to select what he wants to do
"""
print(Fore.YELLOW + "\nNew user" + ("-" * 10) + " create new account")
print(Fore.GREEN + "Returning user" + ("-" * 10) + " login")
print(Fore.RED + "Return later" + ("-" * 10) + "exit\n" + Style.RESET_ALL)

action = {
    "1": "Create new account",
    "2": "Log in to your account",
    "3": "Exit"
}
print(f"1: {action['1']}\n2: {action['2']}\n3: {action['3']}\n")
print("=" * 50)

# START NAVIGATING
while True:
    """
    while loop to make sure you enter a choice
    """
    try:
        print(Fore.LIGHTMAGENTA_EX + "Enter your choice\n" + Style.RESET_ALL)
        choice = int(input())
        if choice > 3 or choice < 1:
            raise ValueError
        break
    except ValueError:
        print("\nEnter: [" + Fore.GREEN + "1, 2 or 3" + Style.RESET_ALL + "]\n")

if choice == 1:
    create_account.create_account()
    log_in.log_in()

elif choice == 2:
    print("=" * 50)
    print(Fore.BLUE + "COMING SOON" + Style.RESET_ALL)
    print("=" * 50)
    print(Fore.RED + "logging in for returning user is not implemented yet, create account then login in"
          + Style.RESET_ALL)
    print(Fore.YELLOW + "redirecting to creating account...\n\n\n" + Style.RESET_ALL)
    for z in range(5):
        time.sleep(1)
    create_account.create_account()
    log_in.log_in()
elif choice == 3:
    exit_app.exit_app()

# SERVICE OPTIONS
print(Fore.LIGHTMAGENTA_EX + f"\nHello {var_global.new_user_name}!! Which service do you want to be offered"
      + Style.RESET_ALL)

services = {
    "1": "ORDER SHOES",
    "2": "TRADE WITH US",
    "3": "UNLOCK DISCOUNT",
    "4": "EXIT"
}

print(Fore.GREEN + f"\n1: {services['1']}\n" + Fore.YELLOW +
      f"2: {services['2']}\n3: {services['3']}\n" +
      Fore.RED + f"4: {services['4']}\n" + Style.RESET_ALL)

print("=" * 50)

while True:
    """
    while loop to make sure you enter a choice
    """
    try:
        choose_service = int(input())
        if choose_service > 4 or choose_service < 1:
            raise ValueError
        break
    except ValueError:
        print("\nEnter: [" + Fore.GREEN + "1, 2, 3 or 4" + Style.RESET_ALL + "]\n")

if choose_service == 1:
    # PRINT THE BRANDS
    brands.print_brands()

if choose_service == 2:
    print("=" * 50)
    print(Fore.BLUE + "COMING SOON" + Style.RESET_ALL)
    print("=" * 50)
    print(Fore.RED + "Trading with us is not implemented yet, kindly VIEW SHOES" + Style.RESET_ALL)
    print(Fore.YELLOW + "redirecting to VIEW SHOES...\n\n\n" + Style.RESET_ALL)
    for z in range(5):
        time.sleep(1)
    brands.print_brands()

if choose_service == 3:
    print("=" * 50)
    print(Fore.BLUE + "COMING SOON" + Style.RESET_ALL)
    print("=" * 50)
    print(
        Fore.RED + "Unlock discount is not implemented yet, kindly VIEW SHOES" + Style.RESET_ALL)
    print(Fore.YELLOW + "redirecting to VIEW SHOES...\n\n\n" + Style.RESET_ALL)
    for z in range(5):
        time.sleep(1)
    brands.print_brands()

if choose_service == 4:
    print(Fore.RED + "exiting app..." + Style.RESET_ALL)
    time.sleep(3)
    exit_app.exit_app()

# CHOOSE BRAND
brand_choose.choose_brand()

# DISPLAY SHOES IN BRAND SELECTED BY USER
display_conditions.print_shoes()

# CHECK IF USER FOUND A SHOE OF THEIR CHOICE
fit_check.check_fit()
