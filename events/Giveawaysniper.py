import selfcord as discord
from selfcord.ext import commands
import time
from cfg.cfg import get_value
from handler import logger

class Giveawaysniper(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            is_sniper = get_value('giveaway_sniper')
            if "GIVEAWAY" in message.content:
                if str(is_sniper) == "True":
                    if message.author.id == 123067977615540225 or 294882584201003009:
                        try:
                            await message.add_reaction("🎉")
                            logger.log_error("events.Giveawaysniper", "info", "Participated in a Giveaway ("+str(message.jump_url)+")")
                        except Exception as e:
                            logger.log_error("events.Giveawaysniper", "error", "An error occurred while entering in Giveaway "+str(e))
            if f"Congratulations <@{self.client.user.id}>" in message.content:
                if message.author.id == 123067977615540225 or 294882584201003009:
                    print("WON!")
                    logger.log_error("events.Giveawaysniper", "info", "You just won a Giveaway ("+str(message.jump_url)+")")
        except Exception as e:
            logger.log_error("events.Giveawaysniper", "error", str(e))

def setup(client):
    client.add_cog(Giveawaysniper(client))
