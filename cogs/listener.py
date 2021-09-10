import discord
from discord.ext import commands
import json
import datetime


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
                    if message.content.startswith('**'):
                        message_raw = message.content
                        message_head = message_raw.split('**')[1]
                        message_body = message_raw.split('**')[2]

                        data = {"headline":message_head, "body":message_body, "img_url": message.attachments[0].url}
                        date_time = datetime.datetime.now().strftime('%m-%d-%Y_%H-%M-%S')
                        with open(f'./json/{date_time}.json', 'a', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, indent=4)
                        embed = discord.Embed(
                            title = message_head,
                            description = message_body,
                            color = discord.Color.blue()
                        )
                        embed.set_image(url=message.attachments[0].url)
                        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                        await message.channel.send(embed=embed)
                        await message.delete()
                    else:
                        await message.add_reaction('❎')
                        return
                else:
                    if 'formathelp' in message.content:
                        return
                    await message.add_reaction('❎')
                    return
                    
    @commands.command()
    async def formathelp(self, ctx):
        embed = discord.Embed(
            title = 'Infos zum Format der Nachricht',
            color = discord.Color.blue(),
            description = "Die Überschrift muss fett geschrieben werden (\**Überschrift**)\nDer Rest in der Nachricht wird als Text verwendet und kann mehrzeilig sein.\n\nAußerdem wird ein Bild benötigt, welches einfach der Anhang der Nachricht ist."
        )
        message = await ctx.send(embed=embed)
        await message.pin()

def setup(client):
    client.add_cog(listener(client))