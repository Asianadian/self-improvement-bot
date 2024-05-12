import os
import discord
import dotenv
import logging as log

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

log.basicConfig(level=log.DEBUG)
log.getLogger().handlers.clear()
log.getLogger().addHandler(defaultHandler)

dotenv.load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
  def __init__(self):
    log.debug('Custom client initiated.')
    super().__init__(intents=discord.Intents.default())

  async def on_ready(self):
    log.debug(f'{client.user} has connected to Discord!')
    log.debug(f'{client.guilds[0]} id: {client.guilds[0].id}')

client = CustomClient()
client.run(DISCORD_TOKEN,log_handler=None)

