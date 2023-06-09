import discord
from discord.ext import commands
from dotenv import load_dotenv
import os



load_dotenv()


bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

async def load_cogs(bot):
    await bot.load_extension("music_cog")
    await bot.load_extension("ai_cog")


@bot.event
async def on_ready():
    await load_cogs(bot)
    print(f"{bot.user} has connected to Discord!")


bot.run(os.getenv("DISCORD_TOKEN"))