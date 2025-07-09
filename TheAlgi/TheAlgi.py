import re
import discord
import json
import os
from discord.ext import commands
from discord import app_commands

# read data from json
with open('data/config.json', 'r', encoding = 'utf-8') as data:
    config = json.load(data)
    if config:
        token = config['TOKEN']

class run(commands.Bot):
    async def on_ready(self):
        print(f'[✅] Logged on as {self.user}!')
        
        try:
            guild = discord.Object(id = 1312472802678411314)
            synced = await self.tree.sync(guild = guild)
            print(f'[✅]Synced {len(synced)} command to guild {guild.id}')
            
        except Exception as e:
            print(f'Error syncing commands; {e}')

        # load cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                #-3 để xóa đuôi file
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'[✅]Loaded cogs.{filename[:-3]}')
        
    async def on_command_error(self, message, error):
        orig = getattr(error, "original", error)
        await message.channel.send('Command này bị lỗi r AHAHAHA')
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('hello'):
            await message.channel.send(f'Hello <@{message.author.id}> nha!!')
        
        pattern = re.compile(r'\b(mixue|misu|susu)\b', re.IGNORECASE)
        if(pattern.search(message.content)):
            await message.channel.send(f'most handsome person')
        
        #IMPORTANT
        await bot.process_commands(message)
            
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')
        
intents = discord.Intents.all()
bot = run(command_prefix = "lqd!", intents = intents, help_command = None)

#ID của server
GUILD_ID = discord.Object(id = 1312472802678411314)


@bot.tree.command(name = "hello", description = "Say Hello!", guild = GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("wsp")
    
@bot.command()
async def hello(message):
    await message.send("yea")

@bot.command(name = 'embed', description = "Prepare for welcome")
async def CheckEmbed(context):
    server = context.guild
    embed = discord.Embed(
        title = f'{server.name}',
        url = "https://discord.gg/vos",
        description = "Tran Binh Nguyen", color = 0x03fca9
    )
    embed.set_thumbnail(url = server.icon.url)
    
    rule_id = 1312472802678411317
    forum_id = 1328395196265926726
    mainchat_id = 1330906795190910997
    
    embed.add_field(name = "Nội quy", value = f"Nhớ đọc <#{rule_id}> để không bị vi phạm nhé!", inline = False)
    embed.add_field(name = "Hỏi bài", value = f"Đến <#{forum_id}> và hỏi bất kì bài tập nào!",inline = False)
    embed.add_field(name = "General", value = f"Lên <#{mainchat_id}> để tương tác với mọi người nè!", inline = False)
    embed.set_footer(text = "Chúc bạn có một ngày vui vẻ!!")
    embed.set_image(url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmh5NWh5N3Uza2I2ZjIxcDd3cDV4bmY3MTJvMWk4Z3VqdjlzaXY1byZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ws6T5PN7wHv3cY8xy8/giphy.gif")
    embed.set_author(
        name = context.author.name,
        url = "https://www.facebook.com/algitect.project", 
        icon_url = context.author.display_avatar.url
    )
    
    await context.send(embed = embed)

#slash
@bot.tree.command(name = "embed", description = "Ember demo", guild = GUILD_ID)
async def printer(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(
        title = f'{guild.name}', 
        url = "https://discord.gg/vos", 
        description = "Le Viet Thanh Nhan", color = 0x03fca9
    )
    embed.set_thumbnail(url = guild.icon.url)
    
    rule_id = 1312472802678411317
    forum_id = 1328395196265926726
    mainchat_id = 1330906795190910997
    
    
    embed.add_field(name = "Nội quy", value = f"Nhớ đọc <#{rule_id}> để không bị vi phạm nhé!", inline = False)
    embed.add_field(name = "Hỏi bài", value = f"Đến <#{forum_id}> và hỏi bất kì bài tập nào!",inline = False)
    embed.add_field(name = "General", value = f"Lên <#{mainchat_id}> để tương tác với mọi người nè!", inline = False)
    embed.set_footer(text = "Chúc bạn có một ngày vui vẻ!!")
    embed.set_image(url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmh5NWh5N3Uza2I2ZjIxcDd3cDV4bmY3MTJvMWk4Z3VqdjlzaXY1byZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ws6T5PN7wHv3cY8xy8/giphy.gif")
    embed.set_author(
        name = interaction.user.name,
        url = "https://www.facebook.com/algitect.project", 
        icon_url = interaction.user.display_avatar.url
    )
    
    await interaction.response.send_message(embed = embed)
    
bot.run(token)