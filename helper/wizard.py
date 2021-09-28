from cli import run
import os
import asyncio
from colorama import init
init()
from colorama import Fore, Style
import json
from cfg.cfg import set_value
from aioconsole import ainput


async def setup_bot():
    try:
        os.system('cls')
        print((Fore.RED + Style.BRIGHT) + '### WELCOME TO SETUP WIZARD ###')
        print((Fore.CYAN + Style.BRIGHT) + '\nThis Setup Wizard Will Easily Configure Your Bot Settings.')
        token = str(await ainput('Enter Your Account Token: '))
        await set_value('token', token)
        nitro = str(await ainput('Do You Want To Enable Nitro Sniper (Yes/No): ')).lower()
        if nitro == 'yes':
            nitro_sniper = "True"
        else:
            nitro_sniper = "False"
        await set_value('nitro_sniper', nitro_sniper)
        giveaway = str(await ainput('Do You Want To Enable Giveaway Sniper (Yes/No): ')).lower()
        if giveaway == 'yes':
            giveaway_sniper = "True"
        else:
            giveaway_sniper = "False"
        await set_value('giveaway_sniper', giveaway_sniper)
        usage = str(await ainput('Do You Want To Enable Global Command Usage (Yes/No): ')).lower()
        if usage == 'yes':
            global_usage = "True"
        else:
            global_usage = "False"
        await set_value('global_usage', global_usage)
        logs = str(await ainput('Do You Want To Enable Error Logging (Yes/No): ')).lower()
        if logs == 'yes':
            log_error = "True"
        else:
            log_error = "False"
        await set_value('logging', log_error)
        prefix = str(await ainput('What Should Be The Prefix For Your Selfbot: '))
        await set_value('prefix', prefix)
        owner = int(await ainput('Enter Owner ID Of The Bot: '))
        await set_value('owner', owner)
        print((Fore.GREEN + Style.BRIGHT) + "\nSETUP COMPLETED RESTART THE PROGRAM TO RUN YOUR BOT!")
        await ainput('PRESS ENTER TO CLOSE...')
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] "+str(e))
        await ainput("PRESS ENTER TO RESTART TO SETUP WIZARD...")
        await setup_bot()