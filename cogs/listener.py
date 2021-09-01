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
                if message.attachments != [] and str(message.attachments[0]).endswith(('.png', '.jpg', '.jpeg')):
                    if message.content.startswith('```') and message.content.endswith('```') and 'Headline:' in str(message.content) and 'Body:' in str(message.content):
                        message_raw = message.content[3:-3]
                        message_head = message_raw.split('Body:')[0].strip().split('Headline:')[1][1:]

                        message_body = message_raw.split('Headline:')[1].split('Body')[1][2:]

                        data = {"headline":message_head, "body":message_body, "img_url": message.attachments[0].url}
                        y = json.dumps(data, indent=4)
                        print(y)
                    else:
                        await message.add_reaction('❌')
                        return
                else:
                    await message.add_reaction('❌')
                    return

    

def setup(client):
    client.add_cog(listener(client))