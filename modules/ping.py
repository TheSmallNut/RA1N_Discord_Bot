from discord.ext import commands
import discord


class Ping(commands.Cog, name="Ping"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


def setup(bot):
    bot.add_cog(Ping(bot))
    print("Ping Cog Loaded")


def teardown(bot):
    print("Ping Cog Unloaded")
