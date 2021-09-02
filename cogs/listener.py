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
                    if message.content.startswith('```') and message.content.endswith('```') and 'Headline:' in str(message.content) and 'Body:' in str(message.content):
                        message_raw = message.content[3:-3]
                        message_head = message_raw.split('Body:')[0].strip().split('Headline:')[1][1:]

                        message_body = message_raw.split('Headline:')[1].split('Body')[1][2:]

                        data = {"headline":message_head, "body":message_body, "img_url": message.attachments[0].url}
                        date_time = datetime.datetime.now().strftime('%m-%d-%Y_%H-%M-%S')
                        with open(f'./json/{date_time}.json', 'a', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, indent=4)
                        await message.add_reaction('✅')
                    else:
                        await message.add_reaction('❎')
                        return
                else:
                    if not 'formathelp' in message.content:
                        await message.add_reaction('❎')
                        return
                    else: return
                    
    @commands.command()
    async def formathelp(self, ctx):
        embed = discord.Embed(
            title = 'Infos zum Format der Nachricht',
            color = discord.Color.blue(),
            description = """Beim Senden der Nachricht muss man auf folgendes achten, damit diese auch vom Bot akzeptiert werden:
                        Die Nachricht muss in einem Codeblock verfasst werden, sprich die gesamte Nachricht befindet sich zwischen \``` \```
                        Außerdem müssen bestimmte Keywords vorhanden sein, damit sie auch angenommen wird. Hier ist ein Codeblock mit allen was benötigt wird:
```
Headline: Hier ist eine Überschrift
Body: Hier
ist
ein Text
der
über
mehrere
Zeilen
geht.
```
Außerdem wird ein Bild benötigt, welches einfach der Anhang der Nachricht ist."""
        )
        message = await ctx.send(embed=embed)
        await message.pin()

def setup(client):
    client.add_cog(listener(client))