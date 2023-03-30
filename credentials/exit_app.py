import sys
import time
from colorama import init, Fore, Style
init()


def exit_app():
    """
    Function to exit user for the app
    """
    print(Fore.RED + "exiting app..." + Style.RESET_ALL)
    time.sleep(3)
    return sys.exit()
