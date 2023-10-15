
import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

# load the environment and fetch the discord token
load_dotenv()
TOKEN = os.getenv( 'DISCORD_TOKEN' )

# the bot command prefix
prefix = 'ci;'

# bot intents
intents = discord.Intents.default()
intents.message_content = True

# load the bot using the intents and the command prefix
bot = commands.Bot( intents = intents, command_prefix = prefix )

# event upon starting the bot
@bot.event
async def on_ready():
    print( f'{bot.user.name} has connected to Discord!' )

# a test command
@bot.command( name = 'test' )
async def test( ctx ):
    response = 'This is a test!'
    await ctx.send( response )

# run the bot with the token
bot.run( TOKEN )
