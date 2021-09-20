import os
import ArgentoTxt

#Discord Imports
import discord
from discord.ext import commands

#passing the token
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#This makes on member commands work
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)

#Prefix
client = commands.Bot(command_prefix = "+")

#Loading the client
class MyClient(discord.Client):
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('Hello'):
            await message.reply('Hello!', mention_author=True)

#Events
@client.event
async def on_ready(): #Says that the bot is ready
    print("Argento Central Module online!")
    await client.change_presence(activity=discord.Activity(name="Sobreviviendo!",  type=discord.ActivityType.playing)) 
    #activity = is the activity it appears to be doing, for example "playing tf2"

#Loading cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("/media/sf_Proyectos/Python/botPython (copy)/cogs"):
    if filename.endswith("py"):
        client.load_extension(f"cogs.{filename[:-3]}")
    else: print(f"{filename} no se pudo cargar")


#More events
@client.event 
async def on_member_join(member): #when a member joins on console
    print(f"{member} entró.")

@client.event 
async def on_member_remove(member): #when a member lefts on console
    print(f"{member} se fue.")

client.run(TOKEN)