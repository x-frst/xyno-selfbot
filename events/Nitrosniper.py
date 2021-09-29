import selfcord as discord
from selfcord.ext import commands
import time
from cfg.cfg import get_value
import re
import requests
from handler import logger

class Nitrosniper(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.token = get_value('token')
        self.headers = {
            'Authorization': self.token
        }

    async def fetch_url(self, url):
        response = requests.post(url, headers=self.headers)
        return str(response.text).lower()

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            is_sniper = get_value('nitro_sniper')
            if "discord.gift/" in message.content:
                if str(is_sniper) == 'True':
                    code = re.search("discord.gift/(.*)", message.content).group(1)
                    if len(code) != 16:
                        logger.log_error("events.Nitrosniper", "info", "Invalid Nitro code!")
                    else:
                        r = await self.fetch_url(f"https://discordapp.com/api/v7/entitlements/gift-codes/{code}/redeem")
                        if "this gift has been redeemed already" in r:
                            logger.log_error("events.Nitrosniper", "info", "This gift code has been redeemed already.")
                        elif "subscription_plan" in r:
                            logger.log_error("events.Nitrosniper", "info", "Successfully claimed Nitro gift!")
                        elif "unknown gift code" in r:
                            logger.log_error("events.Nitrosniper", "info", "Unknown gift code!")
                        else:
                            logger.log_error("events.Nitrosniper", "info", "An unknown error occurred!")
        except Exception as e:
            logger.log_error("events.Nitrosniper", "error", str(e))

def setup(client):
    client.add_cog(Nitrosniper(client))
