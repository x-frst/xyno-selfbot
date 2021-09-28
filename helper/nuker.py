from helper import menu
import os
import asyncio
from colorama import init
init()
from colorama import Fore, Style
import json
from cfg.cfg import get_value
from aioconsole import ainput


async def ban_all(client):
    try:
        os.system('cls')
        print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
        print((Fore.BLUE + Style.BRIGHT) + "\nMASS BAN TOOL")
        cid = int(await ainput('Enter Channel ID Of The Server To Ban: '))
        channel = await client.fetch_channel(cid)
        guild = channel.guild
        botname = str(get_value('botname'))
        confirmation = str(await ainput('[WARNING] Are You Sure You Want To Ban All Members From '+guild.name+'? (Yes/No): '))
        if confirmation == 'yes':    
            print((Fore.YELLOW + Style.BRIGHT) + "[STARTING] Starting The Process, This May Take A While...")
            print((Fore.YELLOW + Style.BRIGHT) + "[STARTING] Starting Banning Members...")
            for member in guild.members:
                try:
                    await member.ban(reason="Banned By "+botname)
                except:
                    continue
            print((Fore.GREEN + Style.BRIGHT) + "[SUCCESS] Banned All Possible Members.")
        elif confirmation == 'no':
            print((Fore.RED + Style.BRIGHT) + "[ABORT] Stopping This Action & Going Back To Main Menu In 5 Seconds...")
            await asyncio.sleep(5.0)
            await menu.show_menu(client)
        else:
            raise Exception("Invalid Confirmation Answer.")            
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await ban_all(client)

async def nuke(client):
    try:
        os.system('cls')
        print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
        print((Fore.BLUE + Style.BRIGHT) + "\nSERVER NUKER TOOL")
        cid = int(await ainput('Enter Channel ID Of The Server To Nuke: '))
        channel = await client.fetch_channel(cid)
        guild = channel.guild
        botname = str(get_value('botname'))
        confirmation = str(await ainput('[WARNING] Are You Sure You Want To Nuke '+guild.name+'? This Action Will Attempt To Ban All Possible Members, Delete All Channels & Roles (Yes/No): '))
        if confirmation == 'yes':
            print((Fore.YELLOW + Style.BRIGHT) + "[STARTING] Starting The Process, This May Take A While...")
            try:
                with open('./data/icons/nuke.jpg', 'rb') as image:
                    await guild.edit(icon=image.read(), banner=None, splash=None, name="Nuked By "+botname)
            except:
                pass
            for c in guild.channels:
                try:
                    await c.delete()
                except:
                    continue
            print((Fore.GREEN + Style.BRIGHT) + "[SUCCESS] Deleted All Possible Channels.")
            print((Fore.YELLOW + Style.BRIGHT) + "[STARTING] Starting Banning Members...")
            for member in guild.members:
                try:
                    await member.ban(reason="Nuked By "+botname)
                except:
                    continue
            print((Fore.GREEN + Style.BRIGHT) + "[SUCCESS] Banned All Possible Members.")
            print((Fore.YELLOW + Style.BRIGHT) + "[STARTING] Starting Roles Deletion...")  
            for role in guild.roles:
                try:
                    await role.delete()
                except:
                    continue
            print((Fore.GREEN + Style.BRIGHT) + "[SUCCESS] Deleted All Possible Roles.")
            await client.leave_guild(guild.id)         
            await ainput("[DONE] NUKED SERVER SUCCESSFULLY! PRESS ENTER TO RETURN MAIN MENU.")
            await menu.show_menu(client)
        elif confirmation == 'no':
            print((Fore.RED + Style.BRIGHT) + "[ABORT] Stopping This Action & Going Back To Main Menu In 5 Seconds...")
            await asyncio.sleep(5.0)
            await menu.show_menu(client)
        else:
            raise Exception("Invalid Confirmation Answer.")
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await nuke(client)