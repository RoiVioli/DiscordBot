import discord
import requests
import json


class myclient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}".format(self.user))

    async def on_message(self, message):  
        if message.author == self.user:
            return
        
        if message.content.startswith("!hello"):  
            await message.channel.send("Hi :)")
        if message.content.startswith("!meme"):
            await message.channel.send(get_meme())

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']
    


        
# Initialisez les intents
intents = discord.Intents.default()
intents.message_content = True

# Créez une instance client
client = myclient(intents=intents)

# Exécutez le bot
client.run("TOKEN")  # Remplacez par votre clé API en toute sécurité
