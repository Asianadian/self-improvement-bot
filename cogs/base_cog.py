from const.points import Points
from discord.ext import commands
from base.formatted_logger import get_formatted_logger

class BaseCog(commands.Cog):
  logging = get_formatted_logger()

  def __init__(self, bot):
    self.bot = bot
    self.cursor = bot.db.cursor

  def apply_points(self, discord_id, points):
    try:
      self.cursor.execute(f"INSERT INTO users (discord_id, total_points) VALUES ('{discord_id}', 0)")
    
    except Exception:
      self.logging.debug(f'User already exists: {discord_id}')

    self.cursor.execute(f"INSERT INTO user_activity (reason, delta, discord_id) VALUES ('{points['reason']}', {points['delta']}, '{discord_id}')")
    
    