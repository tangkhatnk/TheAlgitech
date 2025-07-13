import discord
from discord.ext import commands
import json
import sqlite3
import os

with open('data/config.json', 'r', encoding = 'utf-8') as data:
    config = json.load(data)

prefix = config['PREFIX']

def get_prefix(bot, message): #Chỗ này sẽ được import về lại main.py
    if not message.guild:
        return prefix
    try:
        conn = sqlite3.connect('data/prefixes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT prefix FROM prefixes WHERE guild_id = ?", (message.guild.id,))
        new_prefix = cursor.fetchone()
        conn.close()
        return new_prefix[0] if new_prefix else prefix
    except Exception:
        return prefix

class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.init_database()
        
    def init_database(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        conn = sqlite3.connect('data/prefixes.db')
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS prefixes (guild_id INTEGER PRIMARY KEY, prefix TEXT)"
        )
        conn.commit()
        conn.close()    
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setprefix(self, user, new_prefix: str): #Use command
        server_id = user.guild.id
        
        conn = sqlite3.connect('data/prefixes.db')
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT OR REPLACE INTO prefixes (guild_id, prefix) VALUES (?, ?)",
            (server_id, new_prefix)
        )
        
        conn.commit()
        conn.close()

        await user.send(f"[✅] Prefix mới là `{new_prefix}`")
            
async def setup(bot):
    await bot.add_cog(Prefix(bot))