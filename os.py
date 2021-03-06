# https://discord.com/api/oauth2/authorize?client_id=762622211369598986&permissions=268561520&scope=bot
import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
from decouple import config

print("---> BOT is waking up\n")

bot = commands.Bot(command_prefix=["os!"],case_insensitive=True)
bot.remove_command('help')

def load_cogs():
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_ready():
    print(f'---> Logged in as : {bot.user.name} , ID : {bot.user.id}')
    print(f'---> Total Servers : {len(bot.guilds)}\n')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Otakustan Videos"))
    load_cogs()
    print('\n---> BOT is awake\n')

keep_alive()
bot.run(config("BOT_TOKEN"))