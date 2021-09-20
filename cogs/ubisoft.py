#Ubisoft Functionalities
from importlib.util import decode_source
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
        print(f"Ubisoft cog has been loaded!")
    
    #Commands
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