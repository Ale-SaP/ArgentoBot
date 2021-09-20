#example
import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import context
import ArgentoTxt
import random

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Basics cog has been loaded!")
    
    #Commands

    #Ayuda 
    @commands.command(aliases=["ayuda"])
    async def AYUDA(self, ctx):
        await ctx.send(ArgentoTxt.ayudabasica)

    #information on taxes
    @commands.command(aliases=["impufaq"])
    async def IMPUFAQ(self, ctx):
        await ctx.send(f"{ArgentoTxt.faq}")

    #Ping
    @commands.command(aliases=["ping"])
    async def PING(self, ctx):
        await ctx.send(f"~~~~~Pong~~~~~\n{round(self.client.latency + 1000)}ms")

    #rickroll
    @commands.command(aliases=["rick", "Rick"])
    async def RICK(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    #8BALL
    @commands.command(aliases=["8ball", "8BALL"])
    async def BALL8(self, ctx, question):
        await ctx.send(f"Pregunta: `{question}`\nRespuesta : `{random.choice(ArgentoTxt.responsesOra)}`")

def setup(client):
    client.add_cog(Example(client))