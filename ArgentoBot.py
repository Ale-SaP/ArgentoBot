import discord
from discord.channel import CategoryChannel
from discord.ext import commands
from discord.ext.commands.errors import PartialEmojiConversionFailure
from asyncio.tasks import wait
from logging import StringTemplateStyle
from os import link
import random
import texts


#this makes on member commands work
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)

#prefix
client = commands.Bot(command_prefix = "+")

class MyClient(discord.Client):
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('Hello'):
            await message.reply('Hello!', mention_author=True)

#events
"""What is @client.event? is a piece of code that only runs when a determined thing happens"""

@client.event
async def on_ready(): #says that the bot is ready
    print("Booted!")
    await client.change_presence(activity=discord.Activity(name="Sobreviviendo!",  type=discord.ActivityType.playing)) #activity = is the activity it appears to be doing, for example "playing tf2"

@client.event 
async def on_member_join(member): #when a member joins on console
    print(f"{member} entró.")

@client.event 
async def on_member_remove(member): #when a member lefts on console
    print(f"{member} se fue.")


#commands
"""What is @client.command? is a piece of code that only runs when the bot detects a certain message has been sent, a command"""

#help
@client.command(aliases=["ayuda", "AYUDA", "Ayuda"])
async def ayudabasica(ctx):
    await ctx.send(f"{texts.ayudabasica}")

#hola
@client.command(aliases=["hola", "HOLA"])
async def Hola(ctx):
    await ctx.send("Que tal?")

#ping
@client.command(aliases=["Ping", "PING"])
async def ping(ctx):
    await ctx.send(f"{round(client.latency + 1000)}ms")

#rickroll
@client.command(aliases=["rick", "RICK"])
async def Rick(ctx):
    await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

#8ball, oracle or whatever you choose to call it
@client.command(aliases=["oraculo", "oráculo", "Oráculo", "ORACULO"])
async def Oraculo(ctx, *, question):
    await ctx.send(f"""Pregunta: {question}
    Respuesta : {random.choice(texts.responsesOra)}""")

#a fidel castro speech
@client.command(aliases=["fidel", "FIDEL"])
async def Fidel(ctx):
    await ctx.send("https://youtu.be/IQ3xMrb-PFM?t=56")


#Calculators

errorMessage = "Error, caracter o petición invalida." #well, the error message you want to show
todoslosImpuestos = 1.66 #taxes summed up, details in texts.py

#help calculators
@client.command(aliases=["Calc", "calc", "CALC", "help calc", "HELP CALC", "Help Calc"])
async def Calculadoras(ctx):
    await ctx.send(texts.calchelp)

#Steam
@client.command(aliases=["st", "St", "sT"])
async def ST(ctx, * argument : float):
    if argument[0] == int or float:
        steam = argument[0]
        if steam > 0:
            steamconimpu = steam * todoslosImpuestos
            impuestos = steamconimpu - steam 
            await ctx.send(f"El juego base vale {steam}\n Con impuestos sube a {round(steamconimpu, 3)}\n El valor de los impuestos es: {round(impuestos, 3)}")

        else:
            await ctx.send(errorMessage)
    else:
        await ctx.send(errorMessage)

#Steam Items
@client.command(aliases=["sti", "Sti"])
async def STI(ctx, * argument : float):
    tubien = argument[0]
    bien = tubien * todoslosImpuestos
    tubiencomision = tubien * 0.90
    tubienfinal = tubiencomision * todoslosImpuestos
    if tubien > 0:
        await ctx.send(f"Tu item de steam marketplace vale {tubien}\n Si fueras a comprarlo cargando plata a Steam saldria {round(bien, 3)}\n Al venderlo en marketplace vale {round(tubiencomision, 3)}\n Por tanto, su precio de venta en dinero real es {round(tubienfinal, 3)}")
    else:
        await ctx.send(errorMessage)

#Calculadora científica
@client.command(aliases=["cc", "cC", "Cc"])
async def CC(ctx, * argument : float):

    usableNumber = argument[0]
    exponent = 0
    
    if usableNumber > 0: #first module, positives
        while 1 > usableNumber: #usableNumber is less than 1
            exponent += 1
            usableNumber = usableNumber * 10
            if exponent > 65: break
            if 1 <= usableNumber: await ctx.send(f"""En Notación Científica = {round(usableNumber, 8)} ** -{exponent}""")
        while 10 < usableNumber : #usableNumber is ten or more
            exponent +=1
            usableNumber = usableNumber/10
            if exponent > 65: break
            if 10 >= usableNumber: await ctx.send(f"""En Notación Científica = {round(usableNumber, 8)} ** {exponent}""")

    elif usableNumber < 0:  #second module, negatives
        while usableNumber >= -1: #usableNumber is more than -1
            exponent += 1
            usableNumber = usableNumber * 10
            if exponent > 65: break
            if usableNumber > -10: await ctx.send(f"""En Notación Científica = {(round(usableNumber, 8))} ** -{exponent}""")
        while -10 >= usableNumber: #usableNumber is less than -10
            exponent += 1
            usableNumber = usableNumber/10
            if exponent > 65: break
            if -10 < usableNumber: await ctx.send(f"""En Notación Científica = {(round(usableNumber, 8))} ** {exponent}""")
    else: await ctx.send(f"{errorMessage}")

#impuestos details
@client.command()
async def impufaq(ctx):
    await ctx.send(f"{texts.faq}")


# steam scraper
# so yeah, it takes the link and searches for the specific class in the html, then it makes a lot of changes for it to be a float
# I am not sure if its the most effient way of doing this but its how I managed to do it

@client.command(aliases=["STS", "Sts"])
async def sts(ctx, * argument : str):
    from bs4 import BeautifulSoup
    import requests
    import lxml

    stlink = argument[0] #steam link = the argument
    #here starts the html processing
    r = requests.get(stlink)
    soup = BeautifulSoup(r.content, "lxml")
    price = soup.find("div", class_="game_purchase_price price").text
    name = soup.find("div", class_="apphub_AppName").text

    #the result has a lot of empty space and non usable characters, this should clear it
    price = price.strip()
    if price != "Free": #checks if the game is not free, foolproof
        price = price.strip("ARS$ ")

        #steam dot --> py nothing
        #steam comma --> py dot
        price = price.replace(".", "")
        price = price.replace(",", ".")
        price = float(price)

        #now that it is a float, it will calculate the taxes
        steamconimpu = price * todoslosImpuestos
        impuestos = steamconimpu - price

        await ctx.send(f"El juego es {name}\nVale {price}\nCon impuestos sube a {round(steamconimpu, 2)}\nEl valor de los impuestos es: {round(impuestos, 2)}")
    else: await ctx.send(f"El juego es {name}, es gratuito")

client.run("")