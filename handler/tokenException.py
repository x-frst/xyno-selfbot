from colorama import init
init()
from colorama import Fore, Style

def tokenError(error):
    print((Fore.RED + Style.BRIGHT) + f'[ERROR] Raised Token Exception: {error}')