from colorama import init
init()
from colorama import Fore, Style, Back
import os
import asyncio
import json
import sys
from helper import spammer
from cfg.cfg import get_value, set_value
import helper
from helper import security
from aioconsole import ainput
from helper import nuker
from helper import farm

# CLEAR ALL
os.system('cls')


async def giveaway_sniper(client):
    os.system('cls')
    print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
    print((Fore.BLUE + Style.BRIGHT) + "\nGIVEAWAY SNIPER SETTINGS")
    option = str(await ainput('\nEnter Enable/Disable To Change The Settings: '))
    if option.lower() == 'enable':
        val = 'True'
    elif option.lower() == 'disable':
        val = 'False'
    else:
        print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered! Resetting In 5 Seconds...")
        await asyncio.sleep(5.0)
        await giveaway_sniper(client)
    await set_value('giveaway_sniper', val)
    print((Fore.GREEN + Style.BRIGHT) + "Successfully " +option.title()+ "d Option! Returning To Main Menu In 5 Seconds...")
    await asyncio.sleep(5.0)
    await show_menu(client) 

async def nitro_sniper(client):
    os.system('cls')
    print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
    print((Fore.BLUE + Style.BRIGHT) + "\nNITRO SNIPER SETTINGS")
    option = str(await ainput('\nEnter Enable/Disable To Change The Settings: '))
    if option.lower() == 'enable':
        val = 'True'
    elif option.lower() == 'disable':
        val = 'False'
    else:
        print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered! Resetting In 5 Seconds...")
        await asyncio.sleep(5.0)
        await nitro_sniper(client)
    await set_value('nitro_sniper', val)
    print((Fore.GREEN + Style.BRIGHT) + "Successfully " +option.title()+ "d Option! Returning To Main Menu In 5 Seconds...")
    await asyncio.sleep(5.0)
    await show_menu(client)    


async def global_usage(client):
    os.system('cls')
    print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
    print((Fore.BLUE + Style.BRIGHT) + "\nGLOBAL USAGE SETTINGS")
    option = str(await ainput('\nEnter Enable/Disable To Change The Settings: '))
    if option.lower() == 'enable':
        val = 'True'
    elif option.lower() == 'disable':
        val = 'False'
    else:
        print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered! Resetting In 5 Seconds...")
        await asyncio.sleep(5.0)
        await global_usage(client)
    await set_value('global_usage', val)
    print((Fore.GREEN + Style.BRIGHT) + "Successfully " +option.title()+ "d Option! Returning To Main Menu In 5 Seconds...")
    await asyncio.sleep(5.0)
    await show_menu(client) 

async def logging_manager(client):
    os.system('cls')
    print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
    print((Fore.BLUE + Style.BRIGHT) + "\nERROR LOGS SETTINGS")
    option = str(await ainput('\nEnter Enable/Disable To Change Error Logs Settings: '))
    if option.lower() == 'enable':
        val = 'True'
    elif option.lower() == 'disable':
        val = 'False'
    else:
        print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered! Resetting In 5 Seconds...")
        await asyncio.sleep(5.0)
        await logging_manager(client)
    await set_value('logging', val)
    print((Fore.GREEN + Style.BRIGHT) + "Successfully " +option.title()+ "d Option! Returning To Main Menu In 5 Seconds...")
    await asyncio.sleep(5.0)
    await show_menu(client) 

async def show_menu(client):
    show_logo()
    print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
    print((Fore.CYAN + Style.BRIGHT) + "\n1. Enable/Disable Giveaway Sniper")
    print("2. Enable/Disable Nitro Sniper")
    print("3. Enable/Disable Global Usage")
    print("4. Console Settings")
    print("5. DM Advertiser")
    print("6. Server Spammer")
    print("7. DM Spammer")
    print("8. Server Nuker")
    print("9. Mass Ban Starter")
    print("10. Auto Farm Manager")
    print("11. User Profile Manager")
    print("12. Guild Manager")
    print("13. Exit To Console")
    print("14. Reload Selfbot")
    print("15. Shutdown Selfbot")
    print((Fore.YELLOW + Style.BRIGHT))
    ch = int(await ainput("Input Option Number: "))
    if ch == 1:
        await giveaway_sniper(client)
    elif ch == 2:
        await nitro_sniper(client)
    elif ch == 3:
        await global_usage(client)
    elif ch == 4:
        await security.console_manager(client)
    elif ch == 5:
        await spammer.dm_advertise(client)        
    elif ch == 6:
        await spammer.server_spammer(client)
    elif ch == 7:
        await spammer.dm_spammer(client)
    elif ch == 8:
        await nuker.nuke(client)
    elif ch == 9:
        await nuker.ban_all(client)
    elif ch == 10:
        await farm.init_farm(client)
    elif ch == 11:
        await helper.user_manager(client)          
    elif ch == 12:
        await helper.guild_manager(client)     
    elif ch == 13:
        await helper.console(client)  
    elif ch == 14:
        await helper.reload_modules(client)                  
    elif ch == 15:
        await helper.shutdown(client)

def show_logo():
    os.system('cls')
    print((Fore.RED + Back.CYAN + Style.BRIGHT)) # Add bg color
    print(
"""
██╗  ██╗██╗   ██╗███╗   ██╗ ██████╗ 
╚██╗██╔╝╚██╗ ██╔╝████╗  ██║██╔═══██╗
 ╚███╔╝  ╚████╔╝ ██╔██╗ ██║██║   ██║
 ██╔██╗   ╚██╔╝  ██║╚██╗██║██║   ██║
██╔╝ ██╗   ██║   ██║ ╚████║╚██████╔╝
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ 
"""
    )
    print(Style.RESET_ALL)


def show_console_logo():
    os.system('cls')
    print((Fore.CYAN + Back.BLACK + Style.BRIGHT)) # Add bg color
    print(
"""
██   ██        ██████  ██████  ███    ██ ███████  ██████  ██      ███████ 
 ██ ██        ██      ██    ██ ████   ██ ██      ██    ██ ██      ██      
  ███   █████ ██      ██    ██ ██ ██  ██ ███████ ██    ██ ██      █████   
 ██ ██        ██      ██    ██ ██  ██ ██      ██ ██    ██ ██      ██      
██   ██        ██████  ██████  ██   ████ ███████  ██████  ███████ ███████ 
"""
    )
    print(Style.RESET_ALL)