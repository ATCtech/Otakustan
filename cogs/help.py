import discord
from discord.ext import commands

help_desc="""
prefix : `os!`

developed by `weeblet~kun#1193`
"""

class Help(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def help(self,ctx):
    e=discord.Embed(title="Need Help?",description=help_desc,color=0xFFFFFF)
    await ctx.send(embed=e)

  
  @commands.command(pass_context=True)
  async def ping(self,ctx):
    await ctx.send(f'Latency : `{str(self.bot.latency*1000)[:4]}ms`!')

  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author.id == self.bot.user.id:
      return
    for ping in message.mentions:
      if ping.id == self.bot.user.id:
        await message.channel.send(f"Yo {message.author.mention}, my prefix is `os!`")
  
def setup(bot):
  bot.add_cog(Help(bot))
  print('---> HELP LOADED')
