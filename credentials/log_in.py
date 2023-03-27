from colorama import init, Fore, Style
import getpass
from credentials import var_global
init()

"""
LOG IN TO YOUR ACCOUNT
"""


def log_in():
    """"
    :Function to log in
    """
    print("-" * 50)
    print(Fore.BLUE + "LOG IN TO YOUR ACCOUNT" + Style.RESET_ALL)
    print("-" * 50)
    while True:
        # INVISIBLE LOG_IN PASSWORD INPUT and VISIBLE USER_NAME INPUT
        try:
            print("Enter your username")
            log_in_username = input().strip()
            your_password = getpass.getpass(prompt="Enter your password: ", stream=None)
            print("")
            if log_in_username != var_global.new_user_name or your_password != var_global.password:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "username or password is incorrect...try again with correct credentials" + Style.RESET_ALL)

    print(Fore.GREEN + "LOGGED IN SUCCESSFULLY" + Style.RESET_ALL)

