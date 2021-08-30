import discord
from discord.ext import commands
import json
import os

with open("config.json", "r") as f:
    data = json.load(f)
TOKEN = data["token"]

client = commands.Bot(command_prefix='if!', intents = discord.Intents.default(), case_insensitive=True)

@client.event
async def on_ready():
    print('\nReady!\n')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)