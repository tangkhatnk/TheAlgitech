import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    
    async def on_member_join(self, member):
        server = member.guild
        channel = self.bot.get_channel(1393170518240264233) #Drop ID Welcome
    
        embed = discord.Embed(
            title = f'{server.name}',
            url = "https://www.facebook.com/algitect.project",
            description = f'{member.mention} đã đến với Server Discord của **{server.name}**',
            color = 0xc603fc
        )
        
        rule_id = 1312472802678411317
        forum_id = 1328395196265926726
        mainchat_id = 1330906795190910997
        
        embed.set_thumbnail(url = server.icon.url)
        embed.add_field(name = "Nội quy", value = f"Nhớ đọc <#{rule_id}> để không bị vi phạm nhé!", inline = False)
        embed.add_field(name = "Hỏi bài", value = f"Đến <#{forum_id}> và hỏi bất kì bài tập nào!",inline = False)
        embed.add_field(name = "General", value = f"Lên <#{mainchat_id}> để tương tác với mọi người nè!", inline = False)
        embed.set_footer(text = "Chúc bạn có một ngày vui vẻ!!")
        embed.set_image(url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmh5NWh5N3Uza2I2ZjIxcDd3cDV4bmY3MTJvMWk4Z3VqdjlzaXY1byZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ws6T5PN7wHv3cY8xy8/giphy.gif")
        embed.set_author(
            name = member.name,
            url = "https://www.facebook.com/algitect.project", 
            icon_url = member.display_avatar.url
        )
        
        await member.send(embed = embed) #Gửi Direct message
        await channel.send(embed = embed) #Gửi lên Chat của Server

async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))