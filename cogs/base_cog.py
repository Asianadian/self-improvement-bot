from const.points import Points
from discord.ext import commands

class BaseCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.cursor = bot.db.cursor

  def apply_points(self, discord_id, points):
    try:
      self.cursor.execute(f"INSERT INTO users (discord_id, total_points) VALUES ('{discord_id}', 0)")
    
    except Exception:
      print('already')

    self.cursor.execute(f"INSERT INTO user_activity (reason, delta, discord_id) VALUES ('{points['reason']}', {points['delta']}, '{discord_id}')")
    
    