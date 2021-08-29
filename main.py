import discord

key = "ODgxMjY2OTc0MjA0NzY4MzY2.YSqV0w.YVcKJIE_HIAI4uvP3_JqpTQ4xNI"

class FileWatcherClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}! Ready to go!')
        print(f'{self.emojis}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if self.user in message.mentions:
            print(f'Pinged by {message.author}: {message.content}')
            command = message.content.replace(f'<@!{self.user.id}>', '')
            await message.channel.send(f'{command}')

print('Starting')
client = FileWatcherClient()
client.run(key)
