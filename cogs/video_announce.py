import discord
from discord.ext import commands, tasks
import requests
from decouple import config

api_key = config("YT_API_KEY")
yt_channel_id = "UCcvnNBCZplzRkGCFyzNcwzg"
yt_base_url = "https://www.youtube.com/watch?v="
discord_channel = 754251633751359498

def get_latest(id:str) -> tuple:
  latest_video = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={id}&part=snippet,id&order=date&maxResults=1"
  recv=requests.get(latest_video)
  js = recv.json()["items"][0]

  title = js["snippet"]["title"]
  url = yt_base_url + js["id"]["videoId"]

  return (title,url)


class Help(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    self.old_url=get_latest(yt_channel_id)[1]
    self.chk_for_new_video.start()
    

  @tasks.loop(seconds=60.0)
  async def chk_for_new_video(self):
    latest = get_latest(yt_channel_id)
    print("checked")
    if latest[1]!=self.old_url:
      self.old_url=latest[1]
      text_channel = self.bot.get_channel(discord_channel)
      await text_channel.send(f"@everyone We uploaded a new video **{latest[0]}** check it out!\n{latest[1]}")
    




  
def setup(bot):
  bot.add_cog(Help(bot))
  print('---> VIDEO ANNOUNCE LOADED')
