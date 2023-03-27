import time

from colorama import init, Fore, Style
import getpass
from credentials import var_global, del_user_credentials
init()

"""
CREATE NEW ACCOUNT
"""


def create_account():
    """
    :Function to create a new Account for user.
    """
    global password
    var_global.created_accounts = {}
    print("-" * 50)
    print(Fore.BLUE + "CREATE NEW ACCOUNT" + Style.RESET_ALL)
    print("-" * 50 + "\n")

# PROMPT FOR CREDENTIALS

    while True:
        # PROMPT USER_EMAIL
        try:
            print("Enter your email")
            user_email = input().strip().lower()
            if not user_email.endswith("@gmail.com"):
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Not a valid email address" + Style.RESET_ALL)

    while True:
        # PROMPT USER_NAME
        print("Enter username: ")
        var_global.new_user_name = input().strip()
        if var_global.new_user_name:
            break
        else:
            print(Fore.RED + "Required field cannot be empty" + Style.RESET_ALL)

# PROMPT PASSWORD INPUT TYPE (VISIBLE/INVISIBLE)

    while True:
        print(Fore.BLUE + "Create new password ~ atleast 8 characters" + Style.RESET_ALL)
        print("enter: [" + Fore.GREEN + "~yes~" + Style.RESET_ALL + " to see password,"
              + Fore.RED + " ~no~" + Style.RESET_ALL + " to continue invisibly" + Style.RESET_ALL + "]")
        see_password = input().strip().lower()

        if see_password == "no":
            while True:
                # INVISIBLE PASSWORD INPUT
                try:
                    var_global.password = getpass.getpass(prompt='Enter your password: ', stream=None)
                    if len(var_global.password) < 8:
                        raise ValueError
                    break
                except ValueError:
                    print(Fore.RED + "password must be atleast 8 characters" + Style.RESET_ALL)

            while True:
                # INVISIBLE CONFIRM_PASSWORD INPUT
                try:
                    confirm_password = getpass.getpass(prompt='Confirm password', stream=None)
                    if len(confirm_password) < 8 or confirm_password != var_global.password:
                        raise ValueError
                    break
                except ValueError:
                    print(Fore.RED + "password does not match" + Style.RESET_ALL)

            break

        elif see_password == "yes":
            # VISIBLE PASSWORD INPUT
            while True:
                try:
                    print("Enter new password")
                    var_global.password = input().strip()
                    if len(var_global.password) < 8:
                        raise ValueError
                    break
                except ValueError:
                    print(Fore.RED + "password must be atleast 8 characters" + Style.RESET_ALL)

            while True:
                # VISIBLE CONFIRM_PASSWORD INPUT
                try:
                    print("Confirm your password")
                    confirm_password = input().strip()
                    if confirm_password != var_global.password:
                        raise ValueError
                    break
                except ValueError:
                    print(Fore.RED + "password doesn't match" + Style.RESET_ALL)
            break

        else:
            if see_password:
                break
            else:
                print("enter" + Fore.YELLOW + " ~yes~/~no\n" + Style.RESET_ALL)

    var_global.created_accounts[user_email] = {
        "username": var_global.new_user_name,
        "password": var_global.password
    }

    # TO PRINT AND DELETE USER CREDENTIALS IN 10 SECONDS
    print(del_user_credentials.print_and_delete(Fore.RED + "\nCOPY YOUR CREDENTIALS SOMEWHERE SAFE:\n" + Style.RESET_ALL +
                                                "\nCreating account for " + Fore.LIGHTMAGENTA_EX + f"{user_email}" + Style.RESET_ALL
                                                + " with username " + Fore.GREEN + f"{var_global.new_user_name}" + Style.RESET_ALL +
                                                " and password " + Fore.LIGHTBLUE_EX + f"{var_global.password}\n" + Style.RESET_ALL,
                                                Fore.RED + "Copy your credentials somewhere safe" + Style.RESET_ALL +
                                                "Account created for " + Fore.YELLOW + f"{user_email}" + Style.RESET_ALL
                                                + " with username " + Fore.GREEN + f"{var_global.new_user_name}" + Style.RESET_ALL +
                                                " and password " + Fore.LIGHTBLUE_EX + f"{var_global.password}" + Style.RESET_ALL
                                                , 7))

    print("\nconfirm your credentials" + Fore.YELLOW +"[y]" + Style.RESET_ALL + "\ncontinue" + Fore.GREEN + "[n]" +Style.RESET_ALL)
    print(Fore.RED + "\nyou won't be able to see this information again." + Style.RESET_ALL)
    confirm_credentials = input().strip().lower()
    for c in confirm_credentials:
        if c == "y":
            print(var_global.created_accounts)
            time.sleep(5)
            print("\033[H\033[J")
            print(Fore.YELLOW + "redirecting..." + Style.RESET_ALL)
            time.sleep(2)
        else:
            continue
