import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
print(client.run('MTQxOTM1NTE0ODg0MDQ3MjczNw.GkEODO.YHBH5fYh1wShPUC4FXIiIasXkRCPeuU3TTECtE')) # Replace with your own token.