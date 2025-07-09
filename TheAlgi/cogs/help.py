import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="help", description="show commands")
    async def help_prefix(self, ctx):
        embed = discord.Embed(
            title="List commands",
            color=0x58acfc    
        )
        for cmd in self.bot.commands:
            embed.add_field(
                name=f"lqd!{cmd.name}",
                value=cmd.description or "No description frfr",
                inline=False
            )
            
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.display_avatar.url
        )
        await ctx.send(embed=embed)
        
    @discord.app_commands.command(name="help", description="show commands")
    async def help_slash(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="List commands",
            color=0x58acfc
        )
        for cmd in self.bot.commands:
            embed.add_field(
                name=f"lqd!{cmd.name}",
                value=cmd.description or "No description frfr",
                inline=False
            )
        # Hiển thị slash commands
        for cmd in self.bot.tree.get_commands():
            embed.add_field(
                name=f"/{cmd.name}",
                value=cmd.description or "No description frfr",
                inline=False
            )
        embed.set_footer(
            text=f"Requested by {interaction.user.display_name}",
            icon_url=interaction.user.display_avatar.url
        )
        await interaction.response.send_message(embed=embed)
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))