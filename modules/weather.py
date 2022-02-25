from discord.ext import commands
import discord
from API_Imports.weatherAPI import *


class Weather(commands.Cog, name="Weather"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="willItRain", aliases=["willitrain", "wir", "WIR", "rain", "RAIN", "Rain"])
    async def _willItRain(self, ctx: commands.Context, location):
        jsonWeather = getWeather(location)
        chanceOfRain = willItRain(jsonWeather)
        await ctx.send(f"The chance of it raining is **{chanceOfRain}%** in {jsonWeather['location']['name']} {jsonWeather['location']['region']}")


def setup(bot):
    print("Weather Cog Loaded")
    bot.add_cog(Weather(bot))


def teardown(bot):
    print("Weather Cog Unloaded")
