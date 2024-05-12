import asyncio
import discord
import dotenv
import os

from discord.ext import commands
from formatted_logger import getFormattedLogger

logging = getFormattedLogger()

dotenv.load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def load():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'cogs.{filename[:-3]}')

asyncio.run(load())
bot.run(DISCORD_TOKEN,log_handler=None)



