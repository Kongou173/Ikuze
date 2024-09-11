import discord
from zoneinfo import ZoneInfo
from datetime import datetime
import os
from discord.ext import commands
from keep_alive import keep_alive

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_connect():
    print('Bot is connecting...')

@bot.event
async def on_disconnect():
    print('Bot disconnected.')

@bot.command(name='time')
async def time(ctx):
    tz = ZoneInfo('Asia/Tokyo')
    tokyo_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'現在の東京の時間は: {tokyo_time}')

# Keep the bot alive
keep_alive()

# Run the bot
token = os.getenv('DISCORD_BOT_TOKEN')
if token:
    print('Bot token found, running bot...')
    bot.run(token)
else:
    print('Bot token not found. Please set DISCORD_BOT_TOKEN environment variable.')
