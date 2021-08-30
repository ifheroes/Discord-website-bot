import discord
from discord.ext import commands
import json


class listener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author == self.client.user:
            with open("./config.json", "r") as f:
                data = json.load(f)
            channel_id = data["channel_id"]
            if message.channel.id == int(channel_id):
                print(message.content)

    

def setup(client):
    client.add_cog(listener(client))