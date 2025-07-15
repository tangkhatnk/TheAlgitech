import discord
from discord.ext import commands
from discord import app_commands
import datetime

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = 'ticket', value = 'Tạo ticket')
    async def ticket(self, message):
        view = TicketView()
        channel = self.bot.get_channel(1394271134937120930)
        embed = discord.Embed(
            title = f'₊ ๑ Support ! . ⋆',
            description = f"Hello there! If you need any assistance, feel free to open a ticket, and we'll help you as quickly as possible! 💙 \n ✩----------------------------------------------✩ \n click a button below to create your ticket.!!",
            color = 0xc603fc
        )
        await channel.send(embed = embed, view = view) #Cần view mới hiện thị button
        
class TicketView(discord.ui.View):  
    def __init__(self):
        super().__init__(timeout = None)
        
    @discord.ui.button(label = 'Mở Ticket', style = discord.ButtonStyle.primary, emoji = '🎫')
    async def openticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        server = interaction.guild
        user = interaction.user
        staff_role = server.get_role(1313526520584863847)
        
        for check in server.text_channels:
            if check.topic == str(user.id):
                await interaction.response.send_message(
                    f'Bạn đã có ticket {check.mention}',
                    ephemeral = True
                )
                return
        
        permission = {
            server.default_role: discord.PermissionOverwrite(read_messages = False),
            user: discord.PermissionOverwrite(read_messages = True, send_messages = True),
            server.me: discord.PermissionOverwrite(read_messages = True, send_messages = True),
            staff_role: discord.PermissionOverwrite(read_messages = True, send_messages = True),
            
        }
        channel_name = f'ticket・{user.name}'.replace(" ","-").lower()
        
        channel = await server.create_text_channel(
            name = channel_name,
            overwrites = permission,
            reason = f'{user} mở ticket',
            topic = str(user.id), #topic là hàm riêng không đổi tên được
        )
        
        await interaction.response.send_message(f'[✅] Ticket được tạo {channel.mention}', ephemeral = True)
        await channel.send(
            embed = discord.Embed(
            title = "📩 Ticket đã được tạo!",
            description = f"{user.mention}, bạn có thể mô tả vấn đề của mình tại đây.\n\nBấm nút bên dưới để **đóng ticket** khi đã xong.",
            color = 0x00ff99
        ),
        view = CloseTicketView()
)

        
class CloseTicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label=  "❌ Đóng Ticket", style = discord.ButtonStyle.danger)
    async def close(self, user: discord.Interaction, button: discord.ui.Button):
        await user.response.send_message("🔒 Ticket sẽ đóng sau 3 giây.", ephemeral=True)
        await discord.utils.sleep_until(datetime.datetime.utcnow() + datetime.timedelta(seconds = 3))
        await user.channel.delete(reason = "Ticket bị đóng")

async def setup(bot):
    await bot.add_cog(Ticket(bot))
        
        
        