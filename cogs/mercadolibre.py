#Mercado Libre
from os import PRIO_PROCESS, times
import discord
from discord import client
from discord.ext import commands
from discord.ext.commands.core import hooked_wrapped_callback
from requests.api import request

from bs4 import BeautifulSoup
from bs4.element import AttributeValueWithCharsetSubstitution
from discord.ext.commands.errors import PrivateMessageOnly
import requests
import lxml
import ArgentoTxt
import string

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Mercado Libre cog has been loaded!")

    @commands.command(aliases=["Ml", "ML"])
    async def ml(self, ctx, argument):

        if (argument.startswith("https://articulo.mercadolibre.com.ar/") == False) and (argument.startswith("https://www.mercadolibre.com.ar/") == False):
            await ctx.send("Error, ese link no se puede procesar, solo los de https://articulo.mercadolibre.com.ar/ o https://www.mercadolibre.com.ar/ son utilizables")
        
        else:
            #Getting all we need
            r = requests.get(argument)
            soup = BeautifulSoup(r.content, "lxml")

            name = soup.find("h1", class_="ui-pdp-title").text

            #Ap = all prices
            ap = soup.find_all("span", attrs={"class": "price-tag-fraction"})

            #th and td = table headers and table data
            th = soup.find_all("th", attrs={"class": "andes-table__header andes-table__header--left ui-pdp-specs__table__column ui-pdp-specs__table__column-title"})
            td = soup.find_all("td", attrs={"class": "andes-table__column andes-table__column--left ui-pdp-specs__table__column"})

            #ld = list-type description
            ld = soup.find_all("p", attrs={"class": "ui-pdp-family--REGULAR ui-vpp-highlighted-specs__key-value__labels__key-value"})

            #usually in a publication we'll only find th-td or ld, but just in case it will format both

            #Defining the variables we'll be working with
            allPrices = ""
            firstDes = ""
            secondDes = ""
            finalDes = ""
            descriptionList = ""
            timer = 1


            #Extracting the text from the find_all s
            for v in ap:
                allPrices = allPrices + " ~ " + v.get_text()

            for x in th:
                if (x.get_text() != ""):
                    firstDes = firstDes + " ~ " + x.get_text()
                else: break

            for y in td:
                if (y.get_text() != ""):
                    secondDes = secondDes + " ~ " + y.get_text()
                else: break

            for z in ld:
                if (z.get_text() != ""):
                    descriptionList = descriptionList + " ~ " + z.get_text()
                else: break

            #splitting them
            firstDes = firstDes.split("~")
            secondDes = secondDes.split("~")
            allPrices = allPrices.split("~")

            #if the product is on discount, it will search for the second price available
            if (soup.find("s", class_="price-tag ui-pdp-price__part ui-pdp-price__original-value price-tag__disabled") == None):
               price = allPrices[1]
            else:
                price = allPrices[2]

            #adding each th with its corresponding td
            while (timer < len(firstDes)):
                finalDes = finalDes + f" {firstDes[timer]}: {secondDes[timer]}\n"
                timer += 1
            
            #the base message is formed only by name and price
            messageToSend = (f"Nombre: `{name}`\nPrecio: `{price}`")

            #if we find either th-td it will add it to the message, same with the list
            if (descriptionList != ""): messageToSend = f"{messageToSend} \nCaracterísticas del Producto:\n `{descriptionList}`"
            if (finalDes != ""): messageToSend = f"{messageToSend} \nCaracterísticas Principales:\n `{finalDes}`"

            await ctx.send(messageToSend)

def setup(client):
    client.add_cog(Example(client))
