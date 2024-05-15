import discord

from discord.ext import commands

class tasks(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='mwnv')
  async def meal_with_no_video(self, ctx):
    await ctx.send(f'{ctx.message.author.global_name} ate their meal without a video!')

async def setup(bot):
  await bot.add_cog(tasks(bot))