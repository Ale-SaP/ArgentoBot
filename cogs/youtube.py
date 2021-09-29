#Music
from token import ASYNC
import discord
from discord import client
from discord.ext import commands
from discord.player import FFmpegAudio
import youtube_dl

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Youtube cog has been loaded!")

    @commands.command(aliases = ["connect"])
    async def CONNECT(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Conectate primero che!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command(aliases = ["disconnect"])
    async def DISCONNECT(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Conectate primero che!")
        else: await ctx.voice_client.disconnect()
    
    @commands.command(aliases = ["play", "P", "p"])
    async def PLAY(self, ctx, url):
        ctx.voice_client.stop
        FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 6", "options": "-vn"}
        YDL_OPTIONS = {"format":"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info["formats"][0]["url"]
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
        
        await ctx.send("Continuando!")
    
    @commands.command(aliases=["pause"])
    async def PAUSE(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Pausado!")

    @commands.command(aliases=["resume"])
    async def RESUME(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Continuando!")


def setup(client):
    client.add_cog(Example(client))