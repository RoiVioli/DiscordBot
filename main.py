import discord

class myclient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}".format(self.user))

intents = discord.Intents.default()
intents.message_content = True
client = myclient(intents=intents)
client.run("MTMwMzExNjg5NjQxMjg5MzIzNA.GRd9JL.Zvl6dG9_Fp7S2XqeDupVw0KLOHc58RvY1hivbE")
