import traceback
import sys
from selfcord.ext import commands
import selfcord as discord
import json
from handler import logger

class errorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return logger.log_error("Command Error", "error", "Command has been disabled")

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return logger.log_error("Command Error", "error", "Command is not usable in DMs")
            except:
                pass

        elif isinstance(error, commands.CommandOnCooldown):
            try:
                return logger.log_error("Command Error", "error", "Command is on cooldown")
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                return logger.log_error("Command Error", "error", "Could not find that member")

        elif isinstance(error, commands.CheckFailure):
            return logger.log_error("Command Error", "error", "Global usage is disabled")

        return

    @commands.Cog.listener()
    async def on_error(self, ctx, error):
        return logger.log_error("System Error", "error", str(error))

def setup(bot):
    bot.add_cog(errorHandler(bot))
