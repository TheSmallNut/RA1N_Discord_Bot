from discord.ext import commands
import discord


class Embed(commands.Cog, name="Embed"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sendEmbed", aliases=[])
    async def _sendEmbed(self, ctx: commands.Context):
        None


def setup(bot):
    bot.add_cog(Embed(bot))
    print("Embed Cog Loaded")


def teardown(bot):
    print("Embed Cog Unloaded")
