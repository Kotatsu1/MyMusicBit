import discord
from discord.ext import commands
from config import TOKEN



bot = commands.Bot(command_prefix='/',  intents=discord.Intents.all())

async def setup(bot):
    await bot.load_extension("music_cog")

@bot.event
async def on_ready():
    await setup(bot)


bot.run(TOKEN)