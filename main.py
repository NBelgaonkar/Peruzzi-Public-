from discord.ext import commands, tasks
import discord
import os

from config import prefix, discordbotkey

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
  	await bot.change_presence(status=discord.Status.online, activity=discord.Game('Watching Swift Technologies'))


for filename in os.listdir('./commands'):
  	if filename.endswith('.py'):
  	    bot.load_extension(f'commands.{filename[:-3]}')

bot.run(discordbotkey)