#Taxes Functionalities
import string
from typing import Final, final
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
        print(f"Impuestos cog has been loaded!")
    
    #Commands
    @commands.command(aliases=["calchelp"])
    async def CALCHELP(self, ctx):
        await ctx.send(ArgentoTxt.calcHelp)

    #Impuesto Digital
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
            name = soup.find("div", class_="apphub_AppName").text
            prices = ""

            #First of all: we get all the prices
            for x in soup.find_all("div", class_="game_purchase_action_bg"):
                prices = f"{prices} ~ {x.get_text()}"

            #We do this in order to be sure it is the price we want because prices contains all the prices in the page
            prices = prices.strip()
            prices = prices.split("~")
            firstPrice = prices[1].strip()

            #If it can finde free: its free
            if (firstPrice.find("Free") > -1):
                await ctx.send(f"`{name} es gratuito!`")

            #If it can find download: then it is a demo
            elif (firstPrice.find("Download") > -1):
                await ctx.send(f"`{name} tiene/es una demo!`")

            #if you can put it in your cart, then it is a paid game 
            elif (firstPrice.find("Add to Cart") > -1):

                #Getting the last price in the string, works with games on discount and those who are not
                firstPrice = firstPrice.split("$")
                firstPrice = firstPrice[-1]

                #Now, to avoid a million methods() we'll check if its a character we want
                final = ""
                for x in firstPrice:
                    if x.isdigit() == True: 
                        final += x
                    elif x == ",":
                        final += "."
                    
                #Finally, we get a float and then the taxes are calculated
                final = float(final)
                steamConImpu = final * todoslosImpuestos
                impuestos = steamConImpu - final
                await ctx.send(f"El juego es `{name}`\nVale `{final}`\nCon impuestos sube a `{round(steamConImpu, 2)}`\nEl valor de los impuestos es: `{round(impuestos, 2)}`")
            else: 
                await ctx.send("Error")

    #Ubisoft scraping
    @commands.command(aliases=["ubi"])
    async def UBI(self, ctx, argument):
        #First of all, we start by looking if it is a ubisoft official link
        if ((argument.find("https://store.ubi.com") == -1)):
            await ctx.send("Error, ese link no se puede procesar, solo los de https://store.ubi.com son utilizables")
        else:
            #Getting all we need
            r = requests.get(argument)
            soup = BeautifulSoup(r.content, "lxml")

            price = soup.find("div", class_="flex-reverse-order").text
            name = soup.find("span", class_="product-title-wrapper product-name product-header-name").text
            name = name.strip()
            price = price.strip()
            
            #IN the ubisoft store, if a game is free, it has nothing in the price related div, just empty spaces, thats why there is a strip method
            if price == "": await ctx.send(f"El juego es `{name}`\n`Es Gratuito!`")
            else:
                #Now that we know it is not free, price is converted to a float
                price = price.replace(".", "").split("$")
                price = price[1].strip()
                price = price.replace(",", ".")
                price = float(price)
                #Calculating taxes...
                priceConImpu = price * todoslosImpuestos
                impuestos = priceConImpu - price

                #Last part: the description only appears on DLCs for some reason, even though it should be found on games also
                #If it has a Description, it will send it, if it doesnt it wont even try
                if (soup.find("span", class_="product-header-edition similar-with-h2") != None):

                    description = soup.find("span", class_="product-header-edition similar-with-h2").text
                    description = description.split("-")
                    description = description[0].strip()

                    await ctx.send(f"El juego es `{name}`\nMás exactamente `{description}`\nVale `{price}`\nCon impuestos sube a `{round(priceConImpu, 2)}`\nEl valor de los impuestos es: `{round(impuestos, 2)}`")
                else: await ctx.send(f"El juego es `{name}`\nVale `{price}`\nCon impuestos sube a `{round(priceConImpu, 2)}`\nEl valor de los impuestos es: `{round(impuestos, 2)}`")


def setup(client):
    client.add_cog(Example(client))