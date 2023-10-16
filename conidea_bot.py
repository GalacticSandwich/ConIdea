
import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

from wb import get_animal
from wb import get_culture
from wb import get_planet

from lang import get_language

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

# generate a random animal
@bot.command( name = 'animal', help = 'Generate a random description of an animal.' )
async def animal( ctx ):
    response = get_animal()
    await ctx.send( response )

# generate a random culture
@bot.command( name = 'culture', help = 'Generate a random description of a humanoid culture.' )
async def culture( ctx ):
    response = get_culture()
    await ctx.send( response )

# generate a random planet
@bot.command( name = 'planet', help = 'Generate a random description of a planet.' )
async def planet( ctx ):
    response = get_planet()
    await ctx.send( response )

#####

# generate a random language
@bot.command( name = 'language', help = 'Generate a random description of a natural language.' )
async def language( ctx ):
    response = get_language()
    await ctx.send( response )

# run the bot with the token
bot.run( TOKEN )
