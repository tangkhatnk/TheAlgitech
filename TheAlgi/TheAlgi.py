import discord
import json
from discord.ext import commands
from discord import app_commands

with open('data/config.json', 'r', encoding = 'utf-8') as data:
    config = json.load(data)
    if config:
        token = config['TOKEN']
        prefix = config['PREFIX']

intents = discord.Intents.all()

bot = commands.Bot(
    intents = intents,
    command_prefix = prefix,
    help_command = None,
)

cogs: list[str] = [
    "cogs.admin.welcome",
    "cogs.utils.prefix.help",
    "cogs.utils.prefix.hello",
    "cogs.utils.prefix.ping",
]

async def load_cogs() -> None:
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f"[✅] Loaded {cog}")

        except Exception as error:
            print(f"[❌] Error: {cog}: {error}")


@bot.event
async def on_ready() -> None:
    await load_cogs()
    await bot.tree.sync()
    print(f'[✅] Looged on as {bot.user}')


bot.run(token)
    