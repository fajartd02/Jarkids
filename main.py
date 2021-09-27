import discord
import os

import dotenv
dotenv.load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We Have logged in')

client.run(os.getenv('TOKEN'))