#Husos horarios
import discord
from discord import client
from discord.ext import commands
from discord.webhook import AsyncWebhookAdapter
import ArgentoTxt

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Time cog has been loaded!")

    @commands.command(alias=["timehelp"])
    async def TIMEHELP(self, ctx):
        await ctx.send(ArgentoTxt.TimeHelp)

    @commands.command(aliases=["TIME"])
    async def time(self, ctx, * arg):
        day = 0

        ourTZ = ArgentoTxt.allTimeZones["AGT"][0]
        dsTZ = ArgentoTxt.allTimeZones[arg[0].upper()][0]
        print(ourTZ, "ourTZ")
        print(dsTZ, "dsTZ")

        offset = dsTZ - ourTZ
        print(offset, "Offset")
        
        dsTime = float(arg[-1].replace(":", "."))
        if offset > dsTime: 
            dsTime += 24
            day = 1
        print(dsTime, "Discord time")
        final = dsTime - offset

        if day == 1:
            await ctx.send(f"Hora solicitada:`{arg[-1]}`\nZona horaria `{ArgentoTxt.allTimeZones[arg[0].upper()][1]}`\n`En argentina serían las {final} el dia anterior`")
        elif final >= 24: 
            await ctx.send(f"Hora solicitada:`{arg[-1]}`\nZona horaria `{ArgentoTxt.allTimeZones[arg[0].upper()][1]}`\n`En argentina serían las {final - 24} del día siguiente`")
        else: 
            await ctx.send(f"Hora solicitada:`{arg[-1]}`\nZona horaria `{ArgentoTxt.allTimeZones[arg[0].upper()][1]}`\n`En argentina serían las {final}`")
        
    
def setup(client):
    client.add_cog(Example(client))