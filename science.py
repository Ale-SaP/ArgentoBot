#scientiphic calculator

import discord
from discord import client
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Science cog has been loaded!")
    
    @commands.command(aliases=["cc"])
    async def CC(self, ctx, * argument : float):
        errorMessage = "Error, caracter o petición invalida."
        usableNumber = argument[0]
        exponent = 0
        
        if usableNumber > 0: #first module, positives
            while 1 > usableNumber: #usableNumber is less than 1
                exponent += 1
                usableNumber = usableNumber * 10
                if exponent > 65: break
                if 1 <= usableNumber: await ctx.send(f"""En Notación Científica = `{round(usableNumber, 8)} * 10 ** -{exponent}`""")
            while 10 < usableNumber : #usableNumber is ten or more
                exponent +=1
                usableNumber = usableNumber/10
                if exponent > 65: break
                if 10 >= usableNumber: await ctx.send(f"""En Notación Científica = `{round(usableNumber, 8)} * 10 ** {exponent}`""")

        elif usableNumber < 0:  #second module, negatives
            while usableNumber >= -1: #usableNumber is more than -1
                exponent += 1
                usableNumber = usableNumber * 10
                if exponent > 65: break
                if usableNumber > -10: await ctx.send(f"""En Notación Científica = `{(round(usableNumber, 8))} * 10 ** -{exponent}`""")
            while -10 >= usableNumber: #usableNumber is less than -10
                exponent += 1
                usableNumber = usableNumber/10
                if exponent > 65: break
                if -10 < usableNumber: await ctx.send(f"""En Notación Científica = `{(round(usableNumber, 8))} * 10 ** {exponent}`""")
        else: await ctx.send(f"{errorMessage}")


def setup(client):
    client.add_cog(Example(client))