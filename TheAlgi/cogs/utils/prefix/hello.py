import discord
from discord.ext import commands

class HelloPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = "Hello", description = "Chào mẹ mày")
    async def hello_prefix(self, message):
        await message.send(f'Thằng ngu <@{message.author.id}')
        
async def setup(bot: commands.Bot):
    await bot.add_cog(HelloPrefix(bot))