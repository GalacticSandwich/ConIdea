
import os
import discord

from dotenv import load_dotenv

# load the environment and fetch the discord token
load_dotenv()
TOKEN = os.getenv( 'DISCORD_TOKEN' )

# create an alias for the discord client
client = discord.Client( intents = discord.Intents.default() )

# the event which takes place upon starting the bot
@client.event
async def on_ready():
    print( f'{client.user} has connected to Discord!' )

# run the client with the token
client.run( TOKEN )
