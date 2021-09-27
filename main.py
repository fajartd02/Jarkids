import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We Have logged in')

client.run(os.getenv('TOKEN'))