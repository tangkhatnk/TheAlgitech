import discord
from discord.ext import commands

class HelpPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'help', description = 'Show commands')
    async def help_prefix(self, message):
        embed = discord.Embed(
            title = "📜 Help Menu",
            description = "Help list:",
            color = 0x471f91
        )
        for cmd in self.bot.commands:
            embed.add_field(
                name = f"at!{cmd.name}",
                value = cmd.description,
                inline = False
            )
            
        embed.set_footer(
            text = f'Requested by {message.author.display_name}',
            icon_url = message.author.display_avatar.url
        )
        await message.send(embed = embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(HelpPrefix(bot))