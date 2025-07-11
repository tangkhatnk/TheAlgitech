import datetime
import discord
from discord import app_commands
from discord.ext import commands

class PingPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'ping', description = 'Check Ping')
    async def ping_prefix(self, message):
        await message.send(f'**{round(self.bot.latency * 1000)}** ms')

async def setup(bot: commands.Bot):
    await bot.add_cog(PingPrefix(bot))