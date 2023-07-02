from colorama import init, Fore, Style
import getpass
from credentials import var_global, del_user_credentials

init()

"""
CREATE NEW ACCOUNT
"""


def create_account():
    """
    Function to create a new Account for user.
    """
    var_global.created_accounts = {}
    print("-" * 50)
    print(Fore.BLUE + "CREATE NEW ACCOUNT" + Style.RESET_ALL)
    print("-" * 50 + "\n")

# PROMPT FOR CREDENTIALS

    while True:
        # PROMPT USER_EMAIL
        try:
            print(Fore.LIGHTMAGENTA_EX + "Enter your email\n" + Style.RESET_ALL)
            var_global.user_email = input().strip().lower()
            if not var_global.user_email.endswith(".com"):
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Not a valid email address" + Style.RESET_ALL)

    while True:
        # PROMPT USER_NAME
        print(Fore.LIGHTMAGENTA_EX + "\nEnter username\n" + Style.RESET_ALL)
        var_global.new_user_name = input().strip()
        if var_global.new_user_name:
            break
        else:
            print(Fore.RED + "required field cannot be empty" + Style.RESET_ALL)

# PROMPT PASSWORD INPUT TYPE (VISIBLE/INVISIBLE)

    while True:
        print(Fore.BLUE + "Create new password ~ atleast 8 characters" + Style.RESET_ALL)
        print("enter: [" + Fore.GREEN + "~yes~" + Style.RESET_ALL + " to see password,"
              + Fore.RED + " ~no~" + Style.RESET_ALL + " to continue invisibly" + Style.RESET_ALL + "]")
        see_password = input().strip().lower()

        if see_password == "no" or see_password == "n":
            while True:
                # INVISIBLE PASSWORD INPUT
                try:
                    var_global.password = getpass.getpass(prompt=Fore.LIGHTMAGENTA_EX + '\nCreate password\n'
                                                          + Style.RESET_ALL, stream=None)
                    if len(var_global.password) < 8:
                        raise ValueError
                    break
                except ValueError:
                    print(Fore.RED + "password must be atleast 8 characters" + Style.RESET_ALL)

            while True:
                # INVISIBLE CONFIRM_PASSWORD INPUT
                try:
                    confirm_password = getpass.getpass(prompt=Fore.LIGHTMAGENTA_EX + '\nConfirm password\n'
                                                       + Style.RESET_ALL, stream=None)
                    if len(confirm_password) < 8 or confirm_password != var_global.password:
                        raise ValueError
                    break
                except ValueError:
                    print(Fore.RED + "password does not match" + Style.RESET_ALL)

            break

        elif see_password == "yes" or see_password == "y":
            # VISIBLE PASSWORD INPUT
            while True:
                try:
                    print(Fore.LIGHTMAGENTA_EX + "\nCreate password\n" + Style.RESET_ALL)
                    var_global.password = input().strip()
                    if len(var_global.password) < 8:
                        raise ValueError
                    break
                except ValueError:
                    print(Fore.RED + "password must be atleast 8 characters" + Style.RESET_ALL)

            while True:
                # VISIBLE CONFIRM_PASSWORD INPUT
                try:
                    print(Fore.LIGHTMAGENTA_EX + "\nConfirm your password\n" + Style.RESET_ALL)
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

    var_global.created_accounts[var_global.user_email] = {
        "username": var_global.new_user_name,
        "password": var_global.password
    }

    # TO PRINT AND DELETE USER CREDENTIALS IN 9 SECONDS
    if see_password == "yes":
        print(del_user_credentials.print_and_delete(Fore.RED + "\nCOPY YOUR CREDENTIALS SOMEWHERE SAFE:\n" + Style.RESET_ALL
                                                    + "\nCreating account for " + Fore.LIGHTMAGENTA_EX
                                                    + f"{var_global.user_email}" + Style.RESET_ALL + " with username " +
                                                    Fore.GREEN + f"{var_global.new_user_name}" + Style.RESET_ALL +
                                                    " and password " + Fore.LIGHTBLUE_EX + f"{var_global.password}\n" +
                                                    Fore.LIGHTYELLOW_EX + "creating your account...\n" + Style.RESET_ALL,

                                                    Fore.RED + "Copy your credentials somewhere safe" + Style.RESET_ALL +
                                                    "Account created for " + Fore.YELLOW + f"{var_global.user_email}"
                                                    + Style.RESET_ALL + " with username " + Fore.GREEN +
                                                    f"{var_global.new_user_name}" + Style.RESET_ALL +
                                                    " and password " + Fore.LIGHTBLUE_EX + f"{var_global.password}"
                                                    + Style.RESET_ALL, 8))
    else:
        print(del_user_credentials.print_and_delete("\nCreating account for " + Fore.LIGHTMAGENTA_EX
                                                    + f"{var_global.user_email}" + Style.RESET_ALL + " with username " +
                                                    Fore.GREEN + f"{var_global.new_user_name}" + Style.RESET_ALL +
                                                    " and password " + Fore.LIGHTBLUE_EX + "*" * len(var_global.password) + "\n" +
                                                    Fore.LIGHTYELLOW_EX + "creating your account...\n" + Style.RESET_ALL,

                                                    Fore.RED + "Copy your credentials somewhere safe" + Style.RESET_ALL +
                                                    "Account created for " + Fore.YELLOW + f"{var_global.user_email}"
                                                    + Style.RESET_ALL + " with username " + Fore.GREEN +
                                                    f"{var_global.new_user_name}" + Style.RESET_ALL +
                                                    " and password " + Fore.LIGHTBLUE_EX + "*" * len(var_global.password)
                                                    + Style.RESET_ALL, 5))

    print("confirm your credentials" + Fore.YELLOW + "[y]" + Style.RESET_ALL
          + "\ncontinue" + Fore.GREEN + "[n]" + Style.RESET_ALL)
    print(Fore.RED + "\nyou won't be able to see this information again." + Style.RESET_ALL)
    confirm_credentials = input().strip().lower()
    if confirm_credentials == "y":
        # TO PRINT AND DELETE USER CREDENTIALS AGAIN IN 5 SECONDS
        print(del_user_credentials.print_and_delete(f"Account for " + Fore.LIGHTMAGENTA_EX + f"{var_global.user_email} "
                                                    + Style.RESET_ALL + f"with:\nusername: " + Fore.GREEN +
                                                    f"{var_global.created_accounts[var_global.user_email]['username']}"
                                                    + Style.RESET_ALL + f"\npassword: " + Fore.LIGHTBLUE_EX +
                                                    f"{var_global.created_accounts[var_global.user_email]['password']}"
                                                    + Style.RESET_ALL,

                                                    f"Account for" + Fore.LIGHTMAGENTA_EX + f"{var_global.user_email} "
                                                    + Style.RESET_ALL + f"with:\nusername:" + Fore.GREEN +
                                                    f"{var_global.created_accounts[var_global.user_email]['username']}"
                                                    + Style.RESET_ALL + f"password:" + Fore.LIGHTBLUE_EX +
                                                    f"{var_global.created_accounts[var_global.user_email]['password']}"
                                                    + Style.RESET_ALL, 5))
