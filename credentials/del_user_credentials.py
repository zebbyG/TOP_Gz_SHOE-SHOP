import os
import time
from colorama import init, Fore, Style
"""
required modules
"""
init()


def print_and_delete(message, words_to_delete, delay):
    """
    Function to delete credentials after creating account.
    message: Initial message.
    words_to_delete: words to remove for message.
    delay: time to delay before deleting words_to_delete in message.
    """
    print(message)
    time.sleep(delay)
    for word in words_to_delete:
        message = message.replace(word, ' ' * len(word))
    os.system('cls' if os.name == 'nt' else 'clear')
    return Fore.GREEN + "\n" + Style.RESET_ALL
