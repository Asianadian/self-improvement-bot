import os
import discord
import dotenv
import logging

from discord.ext import commands
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

defaultFormatter = Formatter(
  fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
  datefmt="%d/%b/%Y %H:%M:%S"
)

defaultHandler = TimedRotatingFileHandler(
  filename='discord.log', 
  when='D', 
  interval=1, 
  backupCount=1, 
  encoding='utf-8', 
  delay=False,
)

defaultHandler.setFormatter(defaultFormatter)

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().handlers.clear()
logging.getLogger().addHandler(defaultHandler)

dotenv.load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
  
class CustomBot(commands.Bot):
  def __init__(self):
    logging.debug('Bot initiated.')
    super().__init__(command_prefix='!', intents=discord.Intents.default())

  async def on_ready(self):
    logging.debug(f'{self.user.name} has connected to Discord!')
    logging.debug(f'{client.guilds[0]} id: {client.guilds[0].id}')

  async def on_member_join(member):
    return

  async def on_error(event, *args, **kwargs):
    return

client = CustomBot()
client.run(DISCORD_TOKEN,log_handler=None)

