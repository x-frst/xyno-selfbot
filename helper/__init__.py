from helper import menu
import os
import asyncio
from colorama import init
init()
from colorama import Fore, Style
import json
from cfg.cfg import get_value, set_value
import base64
from helper import security
from getpass import getpass
import stdiomask
import sys
import requests
import selfcord as discord
from helper import security
from aioconsole import ainput
import shutil


def is_url_image(image_url):
    try:
        image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif")
        r = requests.head(image_url)
        if r.headers["content-type"] not in image_formats:
            return False
        if r.headers["content-type"] == "image/jpeg" or r.headers["content-type"] == "image/jpg":
            img_type = "jpg"
        elif r.headers["content-type"] == "image/png":
            img_type = "png"
        else:
            img_type = "gif"
        return img_type
    except:
        return False

def download_image(image_url, img_type):
    try:
        response = requests.get(image_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        with open('./data/cache/avatar.'+img_type, 'w+b') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        return True
    except Exception as e:
        print(e)
        return False

async def reload_modules(client):
    os.system('cls')
    extensions = get_value('modules')
    default_extensions = ["events.Nitrosniper", "events.Giveawaysniper", "handler.errorHandler"]
    print((Fore.RED + Style.BRIGHT) + "------------------------ RELOADING COMMANDS ------------------------")
    for extension in extensions:
        try:
            client.reload_extension(extension)
            print(Fore.YELLOW + 'Command Reloaded: {}'.format(extension))
        except Exception as error:
            print(Fore.RED + '[ERROR] Cannot Reload {}: {}'.format(extension, error))
            continue
    print((Fore.RED + Style.BRIGHT) + "------------------------ RELOADING MODULES ------------------------")
    for default_extension in default_extensions:
        try:
            client.reload_extension(default_extension)
            print(Fore.YELLOW + 'Module Reloaded: {}'.format(default_extension))
        except Exception as error:
            print(Fore.RED + '[ERROR] Cannot Reload {}: {}'.format(default_extension, error))
            continue
    print(Fore.GREEN + 'Reloading Selfbot Completed')
    await ainput("PRESS ENTER TO RETURN TO CONSOLE...")
    await console(client)

async def shutdown(client):
    try:
        for guild in client.guilds:
            await guild.voice_client.disconnect()
    except:
        pass
    print((Fore.RED + Style.BRIGHT) + 'Process Exiting In 3 Seconds...')
    await asyncio.sleep(3.0)
    await client.close()  
    sys.exit()

async def console(client):
    menu.show_console_logo()
    print((Fore.GREEN + Style.BRIGHT) + "Connected Users: " + str(len(client.users)) + "                   Connected Guilds: " + str(len(client.guilds)))
    print("Nitro Sniper: " + str(get_value('nitro_sniper')) + "                    Giveaway Sniper: " + str(get_value('giveaway_sniper')))
    print("Keycode Set: " + str(get_value('keycode_set')) + "                    Log Errors: " + str(get_value('logging')))
    print("Global Usage: " + str(get_value('global_usage')) + "                   Selfbot Prefix: " + str(get_value('prefix')))
    print("Selfbot ID: " + str(client.user.id) + "        Selfbot Name: " + str(client.user.name))
    print((Fore.MAGENTA + Style.BRIGHT) + "\n[COMMANDS]: Terminal Commands Are Menu, Shutdown, Reload.")
    ch = str(await ainput("[HELP] Enter Console Command To Execute: ")).lower()
    if ch == 'menu':
        await security.is_protected(client)
    elif ch == 'shutdown':
        await shutdown(client) 
    elif ch == 'reload':
        await reload_modules(client)
    else:
        print((Fore.RED + Style.BRIGHT) + "[INVALID] Wrong Command Entered.")
        await ainput("PRESS ENTER TO RESTART TO CONSOLE...")
        await console(client)

async def user_manager(client):
    os.system('cls')
    print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
    print((Fore.BLUE + Style.BRIGHT) + "\nUSER PROFILE MANAGER")
    print((Fore.CYAN + Style.BRIGHT) + "1. Set Your New Username")
    print("2. Change Your Avatar/Profile Picture")
    print("3. Set Your About Me")
    print("4. Change Discord Hypesquad House")
    print("5. Set Your Online Status")
    print("6. Set Your Playing Status")
    print("7. Manage Your Friends")
    print("8. Go Back To Main Menu")
    print((Fore.YELLOW + Style.BRIGHT))
    try:
        option  = int(await ainput('Input Option Number: '))
        if option == 1:
            newname = str(await ainput('Enter Your New Username: '))
            password = str(stdiomask.getpass('Enter Your Discord Password: '))
            try:
                await client.user.edit(username=newname, password=password)
                print((Fore.GREEN + Style.BRIGHT) + "Successfully Set The New Username! Resetting Screen In 5 Seconds...")
                await asyncio.sleep(5.0)
                await user_manager(client)            
            except Exception as e:
                print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
                await ainput("PRESS ENTER TO RESTART FUNCTION.")
                await user_manager(client)   
        elif option == 2:
            avatar_url = str(await ainput('Enter Avatar URL: '))
            try:
                img_type = is_url_image(avatar_url)
                if img_type:
                    dl = download_image(avatar_url, img_type)
                    if dl:
                        with open('./data/cache/avatar.'+img_type, 'rb') as image:
                            await client.user.edit(avatar=image.read())
                            print((Fore.GREEN + Style.BRIGHT) + "\nSuccessfully Set The New Avatar! Resetting Screen In 5 Seconds...")
                            await asyncio.sleep(5.0)
                            await user_manager(client)                          
                    else:
                        raise Exception("Failed To Download Image.")
                else:
                    raise Exception("URL Must Contain A Valid Image Type.")
            except Exception as e:
                print((Fore.RED + Style.BRIGHT) + "\n[ERROR] " + str(e))
                await ainput("PRESS ENTER TO RESTART FUNCTION.")
                await user_manager(client) 
        elif option == 3:
            bio = str(await ainput('Enter Your New About Me: '))
            try:
                await client.user.edit(bio=bio)
                print((Fore.GREEN + Style.BRIGHT) + "Successfully Set The New Bio! Resetting Screen In 5 Seconds...")
                await asyncio.sleep(5.0)
                await user_manager(client)            
            except Exception as e:
                print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
                await ainput("PRESS ENTER TO RESTART FUNCTION.")
                await user_manager(client) 
        elif option == 4:
            house = str(await ainput('Enter Hypesquad Name (Bravery/Brilliance/Balance): ')).lower()
            available_houses = ['bravery', 'brilliance', 'balance']
            try:
                if house in available_houses:
                    if house == 'bravery':
                        house = discord.HypeSquadHouse.bravery
                    elif house == 'brilliance':
                        house = discord.HypeSquadHouse.brilliance
                    elif house == 'balance':
                        house = discord.HypeSquadHouse.balance
                    await client.user.edit(house=house)
                    print((Fore.GREEN + Style.BRIGHT) + "Successfully Set The New Hypesquad Badge! Resetting Screen In 5 Seconds...")
                    await asyncio.sleep(5.0)
                    await user_manager(client) 
                else:
                    raise Exception("Invalid Hypesquad Entered.")           
            except Exception as e:
                print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
                await ainput("PRESS ENTER TO RESTART FUNCTION.")
                await user_manager(client)
        elif option == 5:
            status = str(await ainput('Enter Your Online Status (Online/Idle/Dnd/Invisible): ')).lower()
            available_status = ['online', 'dnd', 'invisible', 'idle']
            try:
                if status in available_status:
                    if status == 'online':
                        status = discord.Status.online
                    elif status == 'idle':
                        status = discord.Status.idle
                    elif status == 'dnd':
                        status = discord.Status.dnd
                    elif status == 'invisible':
                        status = discord.Status.invisible
                    await client.change_presence(status=status)
                    print((Fore.GREEN + Style.BRIGHT) + "Successfully Set The Online Status! Resetting Screen In 5 Seconds...")
                    await asyncio.sleep(5.0)
                    await user_manager(client) 
                else:
                    raise Exception("Invalid Status Entered.")           
            except Exception as e:
                print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
                await ainput("PRESS ENTER TO RESTART FUNCTION.")
                await user_manager(client) 
        elif option == 6:
            status = str(await ainput('Enter Your Activity Type (Playing/Streaming/Listening/Watching): ')).lower()
            game = str(await ainput('Enter Your Game Text: '))
            available_status = ['playing', 'streaming', 'listening', 'watching']
            try:
                if status in available_status:
                    if status == 'playing':
                        status = discord.ActivityType.playing
                    elif status == 'streaming':
                        status = discord.ActivityType.streaming
                    elif status == 'listening':
                        status = discord.ActivityType.listening
                    elif status == 'watching':
                        status = discord.ActivityType.watching
                    await client.change_presence(activity=discord.Activity(type=status, name=game))
                    print((Fore.GREEN + Style.BRIGHT) + "Successfully Set The Game Status! Resetting Screen In 5 Seconds...")
                    await asyncio.sleep(5.0)
                    await user_manager(client) 
                else:
                    raise Exception("Invalid Activity Type Entered.")           
            except Exception as e:
                print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
                await ainput("PRESS ENTER TO RESTART FUNCTION.")
                await user_manager(client) 
        elif option == 7:
            print("1. Send Friend Request To User")
            print("2. Remove User From Friend List")
            print("3. Get Your Friend List")
            action = int(await ainput('Input Option Number: '))
            try:
                if action == 1:
                    uid = int(await ainput('Enter User ID To Send Friend Request: '))
                    user = await client.fetch_user(uid)
                    await user.send_friend_request()
                    print((Fore.GREEN + Style.BRIGHT) + "Successfully Sent Friend Request To "+str(user)+"! Resetting Screen In 5 Seconds...")
                    await asyncio.sleep(5.0)
                    await user_manager(client)    
                elif action == 2:
                    uid = int(await ainput('Enter User ID To Remove From Friend List: '))
                    user = await client.fetch_user(uid)
                    await user.remove_friend()
                    print((Fore.GREEN + Style.BRIGHT) + "Successfully Removed "+str(user)+" From Friend List! Resetting Screen In 5 Seconds...")
                    await asyncio.sleep(5.0)
                    await user_manager(client)  
                elif action == 3:
                    print("Fetching Your Friend List Please Wait...")
                    users = [user.name+'#'+user.discriminator+' ('+str(user.id)+')' for user in client.user.friends]
                    print((Fore.GREEN + Style.BRIGHT) + "Your Friend List: "+', '.join(users))
                    await ainput("PRESS ENTER TO RETURN TO USER PROFILE MANAGER.")
                    await user_manager(client)  
                else:
                    raise Exception("Invalid Action Entered.")  
            except Exception as e:
                print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
                await ainput("PRESS ENTER TO RESTART FUNCTION.")
                await user_manager(client)              
        elif option == 8:
            print((Fore.RED + Style.BRIGHT) + "Exiting To Main Menu...") 
            await asyncio.sleep(2.0)
            await menu.show_menu(client)      
        else:
            print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered, Press Enter To Restarting Function In 5 Seconds...")
            await asyncio.sleep(5.0)
            await user_manager(client)      
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await user_manager(client)                              

async def guild_manager(client):
    try:
        os.system('cls')
        print((Fore.RED + Style.BRIGHT) + '< ' + str(get_value('botname')).upper() + ' SELFBOT CONTROL PANEL ' + ' >')
        print((Fore.BLUE + Style.BRIGHT) + "\nGUILD MANAGER")
        option  = str(await ainput('Enter Action To Perform (Join/Leave): ')).lower()
        if option == 'join':
            inv = str(await ainput('Enter Invite Code/Link: '))
            await client.join_guild(inv)
            print((Fore.GREEN + Style.BRIGHT) + "Successfully Joined The Guild! Returning To Main Menu In 5 Seconds...")
            await asyncio.sleep(5.0)
            await menu.show_menu(client)
        elif option == 'leave':
            sid = str(await ainput('Enter Guild ID To Perform Action: '))
            await client.leave_guild(sid)
            print((Fore.GREEN + Style.BRIGHT) + "Successfully Left The Guild! Returning To Main Menu In 5 Seconds...")
            await asyncio.sleep(5.0)
            await menu.show_menu(client)
        else:
            print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered, Press Enter To Restarting Function In 5 Seconds...")
            await asyncio.sleep(5.0)
            await guild_manager(client)
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await guild_manager(client)        

async def decode_keycode(key):
    base64_bytes = key.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    decoded_string = string_bytes.decode("ascii")
    return int(decoded_string)

async def set_keycode(client):
    try:
        keycode  = str(stdiomask.getpass('Enter A Numeric Keycode: '))
        try:
            if isinstance(int(keycode), int):
                string_bytes = keycode.encode("ascii")
                base64_bytes = base64.b64encode(string_bytes)
                base64_string = base64_bytes.decode("ascii")
                await set_value('keycode_set', "True")
                await set_value('keycode', str(base64_string))
                print((Fore.GREEN + Style.BRIGHT) + "Successfully Set The New Keycode! Returning To Main Menu In 5 Seconds...")
                await asyncio.sleep(5.0)
                await menu.show_menu(client)     
        except:
            raise Exception("Only Numeric Keys Are Allowed.")      
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await security.keycode_manager(client) 

async def remove_keycode(client):
    try:
        print((Fore.BLUE + Style.BRIGHT) + "Removing Your Keycode Please Wait...")
        await set_value('keycode_set', "False")
        await set_value('keycode', "None")
        await asyncio.sleep(2.5)
        print((Fore.GREEN + Style.BRIGHT) + "Successfully Removed Keycode! Returning To Main Menu In 5 Seconds...")
        await asyncio.sleep(5.0)
        await menu.show_menu(client)          
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] " + str(e))
        await ainput("PRESS ENTER TO RESTART FUNCTION.")
        await security.remove_keycode(client) 