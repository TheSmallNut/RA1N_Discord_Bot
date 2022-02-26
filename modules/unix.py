from discord.ext import commands
import discord
import API_Imports.timeConverter as timeConverter


class Unix(commands.Cog, name="Unix"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unix", aliases=[])
    async def _unix(self, ctx: commands.Context):
        None

    @commands.command(name="time")
    async def _time(self, ctx : commands.Context, *, timeString):
        unixTime = timeConverter.datetimeToUnix(timeConverter.convertStringToDatetime(timeString))
        await ctx.send(f"<t:{unixTime}>")



def setup(bot):
    bot.add_cog(Unix(bot))
    print("Unix Cog Loaded")


def teardown(bot):
    print("Unix Cog Unloaded")
