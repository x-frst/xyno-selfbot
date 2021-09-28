from helper import menu
import os
import asyncio
from colorama import init
init()
from colorama import Fore, Style, Back
import json
from cfg.cfg import get_value
import helper
from getpass import getpass
import stdiomask
from aioconsole import ainput


async def is_protected(client):
    show_lock_logo()
    if str(get_value('keycode_set')) == "False":
        await menu.show_menu(client)
    elif str(get_value('keycode_set')) == "True":
        print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
        print((Fore.BLUE + Style.BRIGHT) + "\nKEYCODE REQUIRED TO ACCESS PANEL")
        keycode = str(stdiomask.getpass('\nEnter Numeric Keycode To Proceed: '))
        decoded = await helper.decode_keycode(get_value('keycode'))
        if str(decoded) == str(keycode):
            await menu.show_menu(client)
        else:
            print((Fore.RED + Style.BRIGHT) + 'Wrong Keycode Entered, Resetting In 3 Seconds...')
            await asyncio.sleep(3.0)
            await is_protected(client)

async def console_manager(client):
    os.system('cls')
    print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
    print((Fore.BLUE + Style.BRIGHT) + "\nCONSOLE MANAGER v1.0")
    print((Fore.YELLOW + Style.BRIGHT) + "\n1. Set The New Keycode For Main Menu")
    print("2. Remove The Keycode From Main Menu")
    print("3. Enable/Disable Error Logging To File")
    try:
        option = int(await ainput('\nInput Option Number: '))
        if option == 1:
            await helper.set_keycode(client)
        elif option == 2:
            await helper.remove_keycode(client)
        elif option == 3:
            await menu.logging_manager(client)
        else:
            print((Fore.RED + Style.BRIGHT) + 'Wrong Option Entered, Resetting In 5 Seconds...')
            await asyncio.sleep(5.0)
            await console_manager(client)
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await console_manager(client) 

def show_lock_logo():
    os.system('cls')
    print((Fore.WHITE + Back.BLACK + Style.BRIGHT)) # Add bg color
    print(
"""
                          .:::.         
                        =##****#+.      
                      .%*=#%#%%=+%:     
          .=******=.  *#==#%##%==+%     
         *#+**++**+** **===+++===+%     
        %=#*      **=%:%+=======+%-     
       +*+*        #=#= +#*===+#*.      
     ..++*=........+++=.  -+===-        
     %*++++++++++++++++%* +@==##        
     %=::::::::::::::-=#*-%===##        
     %=:::::::::::::-==#* +%+=*#        
     %=:::::::::::-====#*:##==*#        
     %=::::::::::-=====#*.*%==*#        
     %=::::::::--======#*:@*==##        
     *#****************#+ :##%=         
                            .                                
"""
    )
    print(Style.RESET_ALL)