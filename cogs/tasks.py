import discord

from cogs.base_cog import BaseCog
from const.points import Points
from discord.ext import commands

class tasks(BaseCog):
  def __init__(self, bot):
    super().__init__(bot)

  @commands.command(name='mwnv')
  async def meal_with_no_video(self, ctx):
    self.apply_points(ctx.message.author.name, Points.TEMP)
    await ctx.send(f'{ctx.message.author.name} ate their meal without a video!')

async def setup(bot):
  await bot.add_cog(tasks(bot))