import discord


try:
    with open('token.txt') as f:
        token = f.read()
except FileNotFoundError:
    token = input('No token.txt found. Enter token here > ')


class FileWatcherClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}! Ready to go!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if self.user in message.mentions:
            print(f'Pinged by {message.author}: {message.content}')
            command = message.content.replace(f'<@!{self.user.id}>', '')
            await message.channel.send(f'{command}')

print('Starting')
client = FileWatcherClient()
client.run(token)
