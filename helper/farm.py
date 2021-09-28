from helper import menu
import os
import asyncio
from colorama import init
init()
from colorama import Fore, Style
import json
from cfg.cfg import get_value
from aioconsole import ainput
import random


async def init_farm(client):
    try:
        os.system('cls')
        print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
        print((Fore.BLUE + Style.BRIGHT) + "\nAUTO FARMING TOOL")
        mode = str(await ainput('Select Your Auto Farming Mode (Simple/Advanced): ')).lower()
        cid = int(await ainput('Enter Channel ID To Send Message: '))
        channel = await client.fetch_channel(cid)
        if mode == 'simple':
            secs = int(await ainput('Enter Delay Of Each Message (In Seconds): '))
            msg = str(await ainput('Enter Text To Send: '))
            lp = asyncio.get_event_loop()
            bg_task = lp.create_task(simple_farm(channel, secs, msg))
        elif mode == 'advanced':
            msgs = []
            msg_count = int(await ainput('Enter Number Of Sequenced Messages To Send: '))
            for i in range(msg_count):
                msg = str(await ainput('Enter Sequenced Message Number '+str(i+1)+': '))
                msgs.append(msg)
            cd_mode = str(await ainput('Enter Delay Mode (Fixed/Random): ')).lower()
            if cd_mode == 'fixed':
                secs = int(await ainput('Enter Delay Of Each Message (In Seconds): '))
                lp = asyncio.get_event_loop()
                bg_task = lp.create_task(advanced_fixed_farm(channel, secs, msgs))
            elif cd_mode == 'random':
                start_index = int(await ainput('Enter Starting Index Of Delay (In Seconds): '))
                end_index = int(await ainput('Enter Ending Index Of Delay (In Seconds): '))
                lp = asyncio.get_event_loop()
                bg_task = lp.create_task(advanced_random_farm(channel, start_index, end_index, msgs))
        await ainput('[START] Farm Started, Press Enter To Stop Auto Farming...')
        bg_task.cancel()
        print((Fore.GREEN + Style.BRIGHT) + "\nCancelled Auto Farm, Returning To Main Menu In 5 Seconds...")
        await asyncio.sleep(5.0)
        await menu.show_menu(client)
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await init_farm(client)


async def simple_farm(channel, secs, msg):
    while True:
        await channel.send(msg)
        await asyncio.sleep(secs)

async def advanced_fixed_farm(channel, secs, msgs):
    while True:
        for msg in msgs:
            await channel.send(msg)
            await asyncio.sleep(secs)

async def advanced_random_farm(channel, start_index, end_index, msgs):
    while True:
        for msg in msgs:
            await channel.send(msg)
            random_sleep = random.randint(start_index, end_index)
            await asyncio.sleep(random_sleep)