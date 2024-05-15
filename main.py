import asyncio
import discord
import dotenv
import os

from base.bot import SIBot

def run():
  dotenv.load_dotenv()
  DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

  intents = discord.Intents.default()
  intents.message_content = True

  bot = SIBot(command_prefix='!', intents=intents)
  bot.initialize()

  bot.run(DISCORD_TOKEN,log_handler=None)

if __name__ == "__main__":
  run()



