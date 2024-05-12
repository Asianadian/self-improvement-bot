import discord

from discord.ext import commands

class template(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='req')
  async def hi(self, ctx):
    await ctx.send('res')

async def setup(bot):
  await bot.add_cog(template(bot))