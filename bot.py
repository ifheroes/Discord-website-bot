import discord

class MyClient(discord.Client):
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('')