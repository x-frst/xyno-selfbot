import selfcord as discord
from selfcord.ext import commands
import time
from cli import check

"""
This is an example cog of basic ping command.
You can create more commands in this folder.
Don't forget to add them in config file (eg. commands.Ban).
"""


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.check(check.check_usage)
    @commands.command(name='ping', help='Get latency between Discord & Bot', usage='ping')
    @commands.guild_only()
    async def _ping(self, ctx):
        if ctx.author.bot == False:
            channel = ctx.channel
            t1 = time.perf_counter()
            await ctx.channel.trigger_typing()
            t2 = time.perf_counter()
            embed = discord.Embed(description="Pong!🏓 {}ms".format(round((t2-t1)*100)), color=0x00ccff)
            embed.set_author(name=ctx.message.author)
            embed.set_footer(text = f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ping(client))
