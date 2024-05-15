import asyncio
import discord
import os

from discord.ext import commands
from base.formatted_logger import get_formatted_logger

class SIBot(commands.Bot):
  logging = get_formatted_logger()

  def __init__(self, command_prefix='!', intents=discord.Intents.default()):
    super().__init__(command_prefix=command_prefix, intents=intents)

  async def load(self):
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        await self.load_extension(f'cogs.{filename[:-3]}')

  def initialize(self):
    asyncio.run(self.load())

  
