import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
wifipassword = os.getenv('VALAFARLAB_WIFI_PASSWORD')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()
    if "wifi" in content and "password" in content:
        await message.channel.send(f"{message.author.mention} the wifi info is:\nName: ValafarLab \nPassword: {wifipassword} \nSecurity: WPA3Personal")

    await bot.process_commands(message)

#in Discord type /cowgif
@bot.command()
async def cowgif(ctx):
    await ctx.send("http://imgur.com/gallery/YiMUiop")     

bot.run(token, log_handler=handler, log_level=logging.ERROR)