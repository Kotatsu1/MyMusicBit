import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()


bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

for filename in os.listdir('./'):
    if filename.endswith('cog.py'):
        bot.load_extension(f"{filename[:-3]}")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


bot.run(os.getenv("DISCORD_TOKEN"))