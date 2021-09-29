import os
from itertools import cycle #to use the loop decorator
import ArgentoTxt

#Discord Imports
import discord
from discord.ext import commands, tasks

#passing the token
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#This makes on member commands work
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)

#Custom help command
class customHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()
    
    async def send_bot_help(self, mapping):
        return await self.get_destination().send(ArgentoTxt.ayudaBasica)

    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)

    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        return await super().send_command_help(command)
    

#Prefix
client = commands.Bot(command_prefix = "+", help_command=customHelpCommand())

#Loading cogs
@client.command()
@commands.has_permissions(manage_messages=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("/media/sf_Proyectos/Python/botPython (copy)/cogs"):
    if filename.endswith("py"):
        client.load_extension(f"cogs.{filename[:-3]}")
    else: print(f"{filename} no se pudo cargar")

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
    change_status.start()
    #activity = is the activity it appears to be doing, for example "playing tf2"


#More events
@client.event 
async def on_member_join(member): #when a member joins on console
    print(f"{member} entró.")

@client.event 
async def on_member_remove(member): #when a member lefts on console
    print(f"{member} se fue.")

#Error messages
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando invalido!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("A tu solicitud le falta una parte!")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("No tenés los permisos suficientes!")

status = cycle(["Demoliendo Hoteles!", "Esperando update de TF2", "Definitivamente no mirando Animé"])

@tasks.loop(minutes=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(TOKEN)