#Husos horarios
import discord
from discord import client
from discord.ext import commands
from discord.webhook import AsyncWebhookAdapter
import ArgentoTxt

allTimeZones = {
            "Nota"  : [0.00, "Las horas de verano USA y Europa van de Marzo a Noviembre, en Australia de Abril a Octubre"],
            "GMT"   : [0.00, "Hora universal coordinada"],
            "UTC"   : [0.00, "Hora universal coordinada"],
            "BST"   : [+1.00, "Hora de verano de Inglaterra"],
            "ECT"   : [+1.00,"Hora de Europa central"],
            "EET"   : [+2.00,"Hora de Europa oriental"],
            "ART"   : [+2.00,"Hora de Egipto (Árabe)"],
            "CEST"  : [+2.00, "Hora de verano de Europa Oriental"],
            "MSK"   : [+3.00, "Hora de Moscú"],
            "EAT"   : [+3.00,"Hora de África oriental"],
            "MET"	: [+3.00,"Hora de Oriente Medio"],

            "NET"	: [+4.00,"Hora de Próximo Oriente"],
            "GST"   : [+4.00,"Hora del Golfo"],

            "IRDT"  : [+4.30, "Hora de día de Irán"],
            "AFT"   : [+4.30, "Hora de Afghanistán"],
            "PLT"	: [+5.00,"Hora de Lahore, Pakistán"],
            "UZT"   : [+5.00, "Hora de Uzbekistán"],
            "IST"	: [+5.30,"Hora de la India y Sri Lanka"],
            "NPT"   : [+5.45, "Hora de Nepal"],
            "BST"	: [+6.00,"Hora de Bangladesh"],
            "MMT"   : [+6.30, "Hora de Myanmar/Birmania"],
            "WIB"   : [+7.00, "Hora de Indonesia Occidental"],
            "VST"	: [+7.00,"Hora de Vietnam"],
            "CST"   : [+8.00,"Hora de China (Si buscás la hora central de Estados Unidos, es CT)"],
            "CTT"	: [+8.00,"Hora de China / Taiwán"],
            "ACWST" : [+8.45, "Hora de Australia (Central Occidental)"],
            "JST"	: [+9.00,"Hora de Japón"],

            "ACT"	: [+9.30,"Hora de Australia (Centro)"],
            "ACST"	: [+9.30,"Hora de Australia (Centro)"],

            "AET"	: [+10.00,"Hora de Australia (Este)"],
            "AEST"	: [+10.00,"Hora de Australia (Este)"],
            #Dos con mismo uso, diferente código

            "LHST"  : [+10.30, "Hora de la isla Lord Howe"],

            "SST"	: [+11.00,"Hora de las Islas Salomón"],
            "SBT"	: [+11.00,"Hora de las Islas Salomón"],

            "NST"	: [+12.00,"Hora de Nueva Zelanda"],
            "ANAT" : [+12.00, "Hora de Anadyr"],
            "CHAST" : [+12.45, "Hora de la isla Chatham"],
            "TOT"   : [+13.00, "Hora de Tonga"],
            "LIND"  : [+14.00, "Hora de las Line Islands"],

            #Negativas
            "AOE"   : [-12.00, "Hora 'Anywhwere on Earth', Pacífico y Islas Baker"],
            "MIT"	: [-11.00,"Hora de las Islas Midway"],
            "NUT"   : [-11.00, "Hora de las islas Niue"],
            "HST"	: [-10.00,"Hora de Hawaii"],
            "MART"  : [-9.30, "Hora de las Islas Marquesas"],
            "HDT"   : [-9.00,"Hora de 'Daylight' de Hawaii."],
            "AST"	: [-9.00,"Hora de Alaska"],
            "AKDT"	: [-8.00,"Hora de 'Dayli9t' del Alaska."],
            "PST"	: [-8.00,"Hora del Pacífico"],
            "PDT"	: [-8.00,"Hora de 'Daylight' del Pacífico."],
            "PNT"	: [-7.00,"Hora de Phoenix"],
            "MST"	: [-7.00,"Hora de las Montañas Rocosas"],
            "CT"	: [-6.00,"Hora central (EEUU y Canadá)"], #También referida como CST, pero también China lo usa así que CT
            "EST"	: [-5.00,"Hora del Este de EE.UU."],
            "IET"	: [-5.00,"Hora de Indiana (Este)"],
            "CDT"	: [-5.00,"Hora de 'Daylight' del Centro de EE.UU."],
            "EDT"	: [-4.00,"Hora de 'Daylight' del Este de EE.UU."],
            "PRT"	: [-4.00,"Hora de Puerto Rico e Islas Vírgenes de EEUU"],
            "CNT"	: [-3.30,"Hora de Terranova (Canadá)"],
            #
            "AGT"	: [-3.00,"Hora de Argentina"],
            #
            "BET"	: [-3.00,"Hora de Brasil (Este)"],
            "NDT"   : [-2.30, "Hora de Nwefoundland, Canadá"],
            "WGST"  : [-2.00, "Hora de verano de Groenlandia occidental"],
            "CAT"	: [-1.00,"Hora de África central"],
            "CVT"   : [-1.00, "Hora de Cabo Verde"],}

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Time cog has been loaded!")

    @commands.command(alias=["timehelp"])
    async def TIMEHELP(self, ctx):
        await ctx.send(ArgentoTxt.timeHelp)

    @commands.command(aliases=["TIME"])
    async def time(self, ctx, * arg):

        day = 0
        ourTZ = allTimeZones["AGT"][0]
        dsTZ = allTimeZones[arg[0].upper()][0]
        offset = dsTZ - ourTZ
        dsTime = float(arg[-1].replace(":", "."))
        if offset > dsTime: 
            dsTime += 24
            day = 1
        final = dsTime - offset
        final = round(final, 2)
        if ((str(final))[-2] == ".") and (int((str(final))[-1]) > 6):
            final = float(final) - 0.6 + 1
        elif ((str(final))[-3] == ".") and (int((str(final))[-2]) > 6):
            final = float(final) - 0.6 + 1
        final = round(final, 2)

        if day == 1:
            await ctx.send(f"Hora solicitada: `{arg[-1]}`\nZona horaria: `{ArgentoTxt.allTimeZones[arg[0].upper()][1]}`\n`En argentina serían las {final} el dia anterior`")
        elif final >= 24: 
            await ctx.send(f"Hora solicitada: `{arg[-1]}`\nZona horaria: `{ArgentoTxt.allTimeZones[arg[0].upper()][1]}`\n`En argentina serían las {final - 24} del día siguiente`")
        else:
            await ctx.send(f"Hora solicitada: `{arg[-1]}`\nZona horaria: `{ArgentoTxt.allTimeZones[arg[0].upper()][1]}`\n`En argentina serían las {final}`")
   
def setup(client):
    client.add_cog(Example(client))