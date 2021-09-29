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
        await ctx.send(ArgentoTxt.ayudaBasica)

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

    #Morse
    @commands.command (aliases=["morse"])
    async def MORSE(self, ctx ,*args):
        textToTranslate = args
        #if the text
        if (textToTranslate[0].startswith(".") == False) and (textToTranslate[0].startswith("-") == False): 

            textToTranslate = str(args)
            #If the text does not start with a dot or a midscore, it will be translated to morse,
            #Latin Alphabet ---> Morse
            
            finalCode = ""
            textToTranslate = ""    #We are basically making a string from the text in the args tuple

            #Adding all the words in the argument, separing them with a slash
            for arg in args: 
                textToTranslate += arg + " / "
            textToTranslate = textToTranslate.upper()

            for element in textToTranslate:         #For each letter in the string
                if (element != " ") and (element != "/"): #Checks if it isnt an empty space or a slash
                    if (element in ArgentoTxt.morseCode): #checks if it exists in its dictionary
                        finalCode = finalCode + " " + ArgentoTxt.morseCode[f"{element}"] #Adds the val by searching the key
                    else:  #if it doesnt, it gives out an error
                        await ctx.send(f"`{element} es un carácter inválido, por tanto no se mostrará`")
                else: finalCode = finalCode + element #If it is a space or a slash, it will be added as such
            await ctx.send(f"En morse es:\n `{finalCode}`")
            
        else:
            textToTranslate = str(args)
            #Now, it will make morse --> human
            textToTranslate = ""

            #Now it makes a string from a list of morse characters
            for arg in args: 
               textToTranslate += arg + " "
            words = ""
            finalCode = ""

            for element in textToTranslate:
                if (element == ".") or (element == "-"):  #If its a dot or dash, it will form the word in morse
                    words += element
                elif (element == "/"):  #If its a slash it will add a space
                    finalCode += " "
                elif (element == " "):   #If it is an empty space (remember that they separate letters), the key for val will be searched
                    for key in ArgentoTxt.morseCode:
                        if ArgentoTxt.morseCode[key] == words:
                            words = ""
                            finalCode += key
            await ctx.send(f"Traducido es:\n `{finalCode}`")
#I am not sure if this is the most effective way to make the translation, as searching each key for a val may consume more resources than to simply make a Morse to Latin dictionary



def setup(client):
    client.add_cog(Example(client))