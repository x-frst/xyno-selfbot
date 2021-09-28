import selfcord as discord
from selfcord.ext import commands
from cfg.cfg import get_value

client = commands.Bot(command_prefix=get_value('prefix'), case_insensitive=bool(get_value('case_insensitive')), user_bot=False, guild_subscription_options = discord.GuildSubscriptionOptions.default())