#Steam Functionalities
import string
import discord
from discord import client
from discord.ext import commands

from bs4 import BeautifulSoup
from bs4.element import AttributeValueWithCharsetSubstitution
from discord.ext.commands.errors import PrivateMessageOnly
import requests
import lxml
import ArgentoTxt

errorMessage = "Error, caracter o petición invalida." #well, the error message you want to show
todoslosImpuestos = 1.66 #taxes summed up, details in texts.py

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Steam cog has been loaded!")
    
    #Commands
    @commands.command(aliases=["CALC"])
    async def calc(self, ctx):
        await ctx.send(ArgentoTxt.calchelp)

    #Steam
    #+ST used to refer to steam, thats why in the code it is mentioned the way it is
    @commands.command(aliases=["st"])
    async def ST(self, ctx, * argument : float):
        if argument[0] == int or float:
            steam = argument[0]
            if steam > 0:
                steamconimpu = steam * todoslosImpuestos
                impuestos = steamconimpu - steam 
                await ctx.send(f"El valor base es `{steam}`\n Con impuestos sube a `{round(steamconimpu, 3)}`\n El valor de los impuestos es: `{round(impuestos, 3)}`")
            else:
                await ctx.send(ArgentoTxt.errorMessage)
        else:
            await ctx.send(ArgentoTxt.errorMessage)

    #Steam Items
    @commands.command(aliases=["sti"])
    async def STI(self, ctx, * argument : float):
        tubien = argument[0]
        bien = tubien * todoslosImpuestos
        tubiencomision = tubien * 0.90
        tubienfinal = tubiencomision * todoslosImpuestos
        if tubien > 0:
            await ctx.send(f"Tu item de steam marketplace vale `{tubien}`\n Si fueras a comprarlo cargando plata a Steam saldria `{round(bien, 3)}`\n Al venderlo en marketplace vale `{round(tubiencomision, 3)}`\n Por tanto, su precio de venta en dinero real es `{round(tubienfinal, 3)}`")
        else:
            await ctx.send(ArgentoTxt.errorMessage)

    #Steam scraping
    @commands.command(aliases=["sts"])
    async def STS(self, ctx, argument):
        if (argument.find("https://store.steampowered.com/app") == -1):
            await ctx.send("Error, ese link no se puede procesar, solo los de https://store.steampowered.com/app son utilizables")
        else:
            r = requests.get(argument)
            soup = BeautifulSoup(r.content, "lxml")
            price = soup.find("div", class_="game_purchase_action_bg").text
            name = soup.find("div", class_="apphub_AppName").text

            #Explanations: if it is free, just the name
            if (price.find("Free") > -1): await ctx.send(f"`{name} es gratuito!`")

            #The booleans are basically checking if it has a demo or if it is temporarily free (in that order)
            elif ((price.find("Download") > -1) or (price.find("Downl") > -1)) or ((price.find("Play Game") > -1) or (price.find("Play") > -1)):
                allPrices = [x.get_text() for x in soup.find_all("div", class_="game_purchase_action_bg")]

                finalPrice = allPrices[1]
                finalPrice = finalPrice.strip()
                finalPrice = finalPrice.strip(".").replace(",", ".")
                finalPrice = finalPrice.strip("Add to Cart")
                finalPrice = finalPrice.strip("ARS")
                finalPrice = finalPrice.strip("\n")
                finalPrice = finalPrice.split("$")

                finalPrice = float(finalPrice[-1])
                steamconimpu = finalPrice * todoslosImpuestos
                impuestos = steamconimpu - finalPrice

                #If its free for some time, it'll search the current price and calculate it
                #If it has a demo, it'll search the current price and calculate it (might not work as intended if the demo is the only option available)
                #I really hope it doesnt break, as it was incredibly painful

                if (price.find("Download") > -1) or (price.find("Downl") > -1): await ctx.send(f"El juego es `{name}`\n`Tiene una demo gratuita`\nVale `{finalPrice}`\nCon impuestos sube a `{round(steamconimpu, 2)}`\nEl valor de los impuestos es: `{round(impuestos, 2)}`")
                else: await ctx.send(f"El juego es `{name}`\n`Es gratuito (por ahora!)`\nVale `{finalPrice}`\nCon impuestos sube a `{round(steamconimpu, 2)}`\nEl valor de los impuestos es: `{round(impuestos, 2)}`")

            #Gets the value of the game, no matter if it is on sale
            else:
                price = price.strip()
                price = price.strip(".").replace(",", ".")
                price = price.strip("Add to Cart")
                price = price.strip("ARS")
                price = price.split("$")

                finalPrice = float(price[-1])
                steamconimpu = finalPrice * todoslosImpuestos
                impuestos = steamconimpu - finalPrice
                await ctx.send(f"El juego es `{name}`\nVale `{finalPrice}`\nCon impuestos sube a `{round(steamconimpu, 2)}`\nEl valor de los impuestos es: `{round(impuestos, 2)}`")

def setup(client):
    client.add_cog(Example(client))