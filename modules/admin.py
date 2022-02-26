from discord.ext import commands
import discord
import os


async def reloadAllModules(self, ctx):
    for filename in os.listdir("./modules"):
        if filename.endswith(".py"):
            self.bot.reload_extension(f"modules.{filename[:-3]}")
            await ctx.send(f"**{filename[:-3]}** module reloaded")


def reloadModule(self, moduleName):
    self.bot.reload_extension(f"modules.{moduleName.lower()}")


class Admin(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name="reload", aliases=[])
    @commands.has_permissions(administrator=True)
    async def _reload(self, ctx: commands.Context, module="all"):
        if module == "all":
            await reloadAllModules(self, ctx)
            await ctx.send("ALL Modules Successfully Reloaded")
        else:
            try:
                reloadModule(self, module)
                await ctx.send(f"**{module}** module reloaded")
            except:
                await ctx.send(f"No module named **{module}**")
    
    @commands.command(name = "load")
    @commands.has_permissions(administrator=True)
    async def _load(self, ctx: commands.Context, module):
        try:
            self.bot.load_extension(f"modules.{module.lower()}")
            await ctx.send(f"**{module}** module loaded")
        except(commands.ExtensionAlreadyLoaded):
            await ctx.send(f"**{module}** module already loaded")
        except(commands.ExtensionNotFound):
            await ctx.send(f"No such module as **{module}**")


def setup(bot):
    print("Admin Cog Loaded")
    bot.add_cog(Admin(bot))


def teardown(bot):
    print("Admin Cog Unloaded")
