from discord.ext import commands
import discord
import os


class Admin(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

    def reloadModules(self):
        for filename in os.listdir("./modules"):
            if filename.endswith(".py"):
                self.bot.reload_extension(f"modules.{filename[:-3]}")


def setup(bot):
    print("Admin Cog Loaded")
    bot.add_cog(Admin(bot))


def teardown(bot):
    print("Admin Cog Unloaded")
