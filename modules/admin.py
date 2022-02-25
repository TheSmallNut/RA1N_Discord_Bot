from discord.ext import commands
import discord
import os


def reloadModules(self):
    for filename in os.listdir("./modules"):
        if filename.endswith(".py"):
            self.bot.reload_extension(f"modules.{filename[:-3]}")


def reloadModule(self, moduleName):
    self.bot.reload_extension(f"modules.{moduleName.lower()}")


class Admin(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reload", aliases=[])
    async def _reload(self, ctx: commands.Context, module="all"):
        if module == "all":
            reloadModules(self)
            await ctx.send("ALL Modules Reloaded")
        else:
            try:
                reloadModule(self, module)
                await ctx.send(f"{module} reloaded")
            except:
                await ctx.send(f"No module named {module}")


def setup(bot):
    print("Admin Cog Loaded")
    bot.add_cog(Admin(bot))


def teardown(bot):
    print("Admin Cog Unloaded")
