import time

from colorama import init, Fore, Style
import getpass
from credentials import var_global, del_user_credentials
init()

"""
LOG IN TO YOUR ACCOUNT
"""


def log_in():
    """"
    :Function to log in
    """
    print(Fore.GREEN + "ACCOUNT CREATED SUCCESSFULLY" + Style.RESET_ALL)
    time.sleep(3)
    print(del_user_credentials.print_and_delete(Fore.YELLOW + "redirecting to log_in..."
                                                + Style.RESET_ALL, "redirecting to log_in...", 3))

    print("-" * 50)
    print(Fore.BLUE + "LOG IN TO YOUR ACCOUNT" + Style.RESET_ALL)
    print("-" * 50)
    while True:
        # INVISIBLE LOG_IN PASSWORD INPUT and VISIBLE USER_NAME INPUT
        try:
            print(Fore.LIGHTMAGENTA_EX + "\nEnter your username\n" + Style.RESET_ALL)
            log_in_username = input().strip()
            your_password = getpass.getpass(prompt=Fore.LIGHTMAGENTA_EX + "\nEnter your password:\n"
                                            + Style.RESET_ALL, stream=None)
            print("")
            if log_in_username != var_global.new_user_name or your_password != var_global.password:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "username or password is incorrect...try again with correct credentials" + Style.RESET_ALL)

    print(Fore.GREEN + "LOGGED IN SUCCESSFULLY" + Style.RESET_ALL)

