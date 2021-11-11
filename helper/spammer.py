from helper import menu
import os
import asyncio
from colorama import init
init()
from colorama import Fore, Style
import json
from cfg.cfg import get_value
from aioconsole import ainput


async def dm_advertise(client):
    try:
        os.system('cls')
        print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
        print((Fore.BLUE + Style.BRIGHT) + "\nDM ADVERTISING TOOL")
        cid = int(await ainput('Enter Channel ID To Fetch Members From: '))
        channel = await client.fetch_channel(cid)
        print("Fetched Channel: " + "#" + str(channel.name) + " From " + str(channel.guild.name) + ".")
        choice = str(await ainput('Leave Server After Operation (Yes/No)?: ')).lower()
        msg = str(await ainput('Enter Message To Advertise: ')).replace('\\n', '\n')
        success = 0
        fail = 0
        i = 0
        members = [m for m in channel.members if not m.bot]
        for member in members:
            try:
                await member.create_dm()
                await member.send(msg)
                success += 1
            except:
                fail += 1
                pass
            i += 1
            print((Fore.YELLOW + Style.BRIGHT) + "Messages Sent: "+str(success)+"        Messages Failed: "+str(fail)+"        Members: "+str(i)+"/"+str(len(members)), end="\r")
            await asyncio.sleep(1.3)
        print()
        if choice == 'yes':
            await channel.guild.leave()
        print((Fore.GREEN + Style.BRIGHT) + "Successfully Advertised To "+str(channel.guild.name)+" Members. Returning To Main Menu In 5 Seconds...")
        await asyncio.sleep(5.0)
        await menu.show_menu(client)
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await dm_advertise(client)

async def dm_spammer(client):
    try:
        os.system('cls')
        print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
        print((Fore.BLUE + Style.BRIGHT) + "\nDM SPAMMING TOOL")
        uid = int(await ainput('Enter User ID To Send Messages: '))
        count = int(await ainput('Enter Number Of Messages To Be Sent: '))
        msg = str(await ainput('Enter Message To Spam: ')).replace('\\n', '\n')
        user = await client.fetch_user(uid)
        await user.create_dm()
        for i in range(count):
            await user.send(msg)
            print((Fore.YELLOW + Style.BRIGHT) + "Messages Sent: "+str(i+1), end='\r')
            await asyncio.sleep(1.3)
        print()
        print((Fore.GREEN + Style.BRIGHT) + "Successfully Sent "+str(count)+" Messages To "+str(user)+". Returning To Main Menu In 5 Seconds...")
        await asyncio.sleep(5.0)
        await menu.show_menu(client)
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await dm_spammer(client)

async def server_spammer(client):
    try:
        os.system('cls')
        print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
        print((Fore.BLUE + Style.BRIGHT) + "\nSERVER SPAMMING TOOL")
        cid = int(await ainput('Enter Channel ID To Send Messages: '))
        count = int(await ainput('Enter Number Of Messages To Be Sent: '))
        msg = str(await ainput('Enter Message To Spam: ')).replace('\\n', '\n')
        channel = await client.fetch_channel(cid)
        for i in range(count):
            await channel.send(msg)
            print((Fore.YELLOW + Style.BRIGHT) + "Messages Sent: "+str(i+1), end='\r')
            await asyncio.sleep(1.3)
        print()
        print((Fore.GREEN + Style.BRIGHT) + "Successfully Sent "+str(count)+" Messages To "+str(channel.guild.name)+" - #"+str(channel.name)+". Returning To Main Menu In 5 Seconds...")
        await asyncio.sleep(5.0)
        await menu.show_menu(client)
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await server_spammer(client)
