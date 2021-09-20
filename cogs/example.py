#example
import discord
from discord import client
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Example cog has been loaded!")
    
def setup(client):
    client.add_cog(Example(client))