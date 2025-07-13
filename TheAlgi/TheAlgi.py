import discord
import json
from discord.ext import commands
from discord import app_commands
from cogs.utils.admin.prefix import get_prefix

with open('data/config.json', 'r', encoding = 'utf-8') as data:
    config = json.load(data)
    if config:
        token = config['TOKEN']
        default_prefix = config['PREFIX']

intents = discord.Intents.all()

bot = commands.Bot(
    intents = intents,
    command_prefix = get_prefix,
    help_command = None,
)

cogs: list[str] = [
    "cogs.sys.welcome",
    "cogs.utils.admin.prefix",
    "cogs.utils.prefix.help",
    "cogs.utils.prefix.hello",
    "cogs.utils.prefix.ping",
    
]

async def load_cogs() -> None:
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            cog_name = cog.split(".")[-1]
            print(f"[✅] Loaded {cog_name}")

        except Exception as error:
            print(f"[❌] Error: {cog}: {error}")


@bot.event
async def on_ready() -> None:
    await load_cogs()
    await bot.tree.sync()
    print(f'[✅] Looged on as {bot.user}')


bot.run(token)
    