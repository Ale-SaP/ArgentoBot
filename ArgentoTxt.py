ayudabasica = ("""`----ArgentoBot 1.1----`
`----Última revisión: 9/2021----`

`---Básicos---`
+PING ---> Pong!.
+RICK ---> RickRoll'ed.
+8BALL ---> Hacele una pregunta y te responde.
+CALC ---> Más datos sobre el uso de las calculadoras.
+MORSE ---> Pasá cualquier texto a morse o viceversa.
+MORSEHELP ---> Ayuda y datos relacionadas a morse.
+CC ---> Convierte a notación científica.

`---Impuestos y Links---`
+ST ---> Calcula impuesto a Servicios Digitales (9/21).
+STI ---> Calcula impuestos sobre Items de Steam (9/21).
+STS ---> Calcula impuestos de Juegos de Steam enviando un link (9/21).
+UBI ---> Calcula los impuestos de la Ubisoft Store enviando un link (9/21).
+ML ---> Enviá un link de Mercado Libre y recibí los datos mas relevantes en el canal.
+IMPUFAQ ---> Datos sobre los impuestos y sus cálculos.

`---Husos horarios---`
+TIME ---> Convierte cualquier hora que le pidas a otra zona horaria.
+TIMEHELP ---> Más detalles de su correcto uso.

`---Streaming de Audio (En desarrollo)---`
+CONNECT ---> El bot se conecta al canal de voz en que estés conectado.
+DISCONNECT ---> El bot se desconecta del canal que estés conectado.
+PLAY o +P ---> Al mandar un link, lo busca y lo pasa en el canal de voz.
+PAUSE ---> Pone la transmisión de audio en pausa.
+RESUME ---> Continua la transmisión.
>Por el momento no existe una lista de reproducción, así que solo reproduce lo último enviado.
>En caso de encontrar algún bug, avisá a los mods.

`>Datazo: los comandos se pueden ingresar en mayúscula o en minúscula`
""")
#+ST used to refer to steam, thats why in the code it is mentioned the way it is

TimeHelp = ("""`----ArgentoBot 1.1----`

La función `+TIME` tiene una manera de usarse definida y estructurada:
+TIME (Zona horaria) (Hora en ese lugar del mundo).
La respuesta contendrá una descripción de la zona horaria solicitada, la hora y el equivalente en la Argentina.
Por ejemplo
`+TIME UTC 10:00`
Respuesta: Hora solicitada:`10:00`, Zona horaria `Hora universal coordinada`, `En argentina serían las 7:00`

Se usaron y adaptaron 2 fuentes elaborar una lista lo más cercano a completa, esas son:
http://publib.boulder.ibm.com/tividd/td/TWS/SC32-1274-02/en_US/HTML/SRF_mst273.htm
https://www.timeanddate.com/time/current-number-time-zones.html
""")

MorseHelp = ("""`----ArgentoBot 1.1----`

`----Funcionamiento----`
Si el primer carácter es un punto o una linea lo va a tomar como morse.
Hay ciertos carácteres que no tienen una traducción directa, como el #, °, o las letras con acentos""")

#Legacy text, no aparent use in latest version (9/21)
calchelp = ('''`----ArgentoBot 1.1 9/21----`

Las calculadoras disponibles por el momento son:
Impuestos digitales: `+ST` + Precio
Items de Steam: `+STI` + Precio
Impuestos de Steam con un link: `+STS` + Link
Impuestos de Ubisoft con un link: `+UBI` + Link
Pasar a notación científica: `+CC` + Número a tratar
Como funcionan y se calculan los impuestos?: `+IMPUFAQ` ''')

faq = ("""`----ArgentoBot 1.1----`

`----Impuestos sobre Steam----`
Iva = 21%
Impuesto PAÍS = 8% 
Resolución 4815/2020 = 35% 
Impuesto de Sellos solamente en =
    La Pampa = 1%
    CABA y Bs As = 2%
    Córdoba = 3%
    Salta = 3.6%
    Rio Negro = 5% 
    Chaco = 5.5%

Todos estos porcentajes se suman, por tanto que:
21 + 8 + 35 + Sellos (Por brevedad, se asume que es 2% Nacional) = 66%
Estos cálculos se pueden aplicar para la mayor parte de compras digitales de plataformas reconocidas por la AFIP en el apartado A.
Información resumida de `https://www.mercadopago.com.ar/ayuda/4063`
Más información en `https://www.afip.gob.ar/iva/servicios-digitales/concepto.asp`

Nota: En caso de que seas responsable inscripto o vivas en Tierra del Fuego, no pagás IVA""")

responsesOra = [
    #si
    "Seguro que si.",
    "No, no, no. Bueno si.",
    "Si o Si.",
    "Si o me voy, corta.",
    "SI",
    "Si, Mandale",

    #tal vez
    "Ponele que si",
    "Preguntale a la Luz Mala",
    "Preguntale al Pobero",
    "Preguntale a tu vieja",
    "Who knows",
    "Perhaps",
    "No one knows",

    #no
    "Ni a palo",
    "no XD",
    "Minga",
    "Negative",
    "Rajá de acá pibe",
    "Nein",
]
morseCode = {
    #Letters
    "A" :  ".-",
    "B" :   "-...",
    "C" :  "-.-.",
    "D" :	"-..",
    "E" :	".",
    "F" :	"..-.",
    "G" :	"--.",
    "H" :	"....",
    "I" :	"..",
    "J" :	".---",
    "K" :	"-.-",
    "L" :	".-..",
    "M" :	"--",
    "N" :	"-.",
    "O" :	"---",
    "P" :	".--.",
    "Q" :	"--.-",
    "R" :	".-.",
    "S" :	"...",
    "T" :	"-",
    "U" :	"..-",
    "V" :	"...-",
    "W" :	".--",
    "X" :   "-..-",
    "Y" :	"-.--",
    "Z" :	"--..",

    #Accents
    "Ñ" :   "--.--",
    "Á" :   ".--.-",
    "É" :   "..-..",
    "Ö" :   "---.",
    "Ü" :   "..--",

    #Numbers
    "1" : 	".----",
    "2" :	"..--- ",
    "3" :	"...--",
    "4" :	"....-",
    "5" :	".....", 	
    "6" :	"-....", 	
    "7" :	"--...", 	
    "8" :	"---..", 	
    "9" :	"----.",
    "0" :	"-----", 

    #Math 
    "+" : ".-.-.",
    "=" : "-...-",
    "." : ".-.-.-",
    ":" : "---...",
    "/" : "-..-.",

    #Punctuation
    "_" : "..--.-",
    ","	: "--..--",
    ";" : "-.-.-.",
    "?" : "..--..",
    "¿" : "..--..",
    "!" : "..--.",
    "¡" : "..-- .",
    "'" : ".----.",
    "-" : "-....-",
    '"' : ".-..-.,",
    "$" : "...-..-",

    #Parenthesys
    "[" : "-.--.",
    "]" : "-.--.-",
    "{" : "-.--.",
    "}" : "-.--.-",
    "(" : "-.--.",
    ")" : "-.--.-",
    }

allTimeZones = {
            "GMT"   : [0, "Hora universal coordinada"],
            "UTC"   : [0, "Hora universal coordinada"],
            "BST"   : [+1, "Hora de verano de Inglaterra"],
            "ECT"   : [+1,"Hora de Europa central"],
            "EET"   : [+2,"Hora de Europa oriental"],
            "ART"   : [+2,"Hora oficial de Egipto (Árabe)"],
            "CEST"  : [+2, "Hora de verano de Europa Oriental"],
            "MSK"   : [+3, "Hora de Moscú"],
            "EAT"   : [+3,"Hora de África oriental"],
            "MET"	: [+3,"Hora de Oriente Medio"],

            "NET"	: [+4,"Hora de Próximo Oriente"],
            "GST"   : [+4,"Hora del Golfo"],

            "IRDT"  : [+4.3, "Hora de día de Irán"],
            "AFT"   : [+4.3, "Hora de Afghanistán"],
            "PLT"	: [+5,"Hora de Lahore, Pakistán"],
            "UZT"   : [+5, "Hora de Uzbekistán"],
            "IST"	: [+5.3,"Hora oficial de la India y Sri Lanka"],
            "NPT"   : [+5.45, "Hora de Nepal"],
            "BST"	: [+6,"Hora oficial de Bangladesh"],
            "MMT"   : [+6.30, "Hora de Myanmar/Birmania"],
            "WIB" : [+7, "Hora de Indonesia Occidental"],
            "VST"	: [+7,"Hora oficial de Vietnam"],
            "CST"   : [+8,"Hora de China (Si buscás la hora central de Estados Unidos, es CT)"],
            "CTT"	: [+8,"Hora de China / Taiwán"],
            "ACWST" : [+8.45, "Hora de Australia (Central Occidental)"],
            "JST"	: [+9,"Hora oficial de Japón"],

            "ACT"	: [+9.3,"Hora de Australia (Centro) (Usada de Abril a Octubre)"],
            "ACST"	: [+9.3,"Hora de Australia (Centro) (Usada de Abril a Octubre)"],

            "AET"	: [+10,"Hora de Australia (Este) (Usada de Abril a Octubre)"],
            "AEST"	: [+10,"Hora de Australia (Este) (Usada de Abril a Octubre)"],
            #Dos con mismo uso, diferente código

            "LHST"  : [+10.30, "Hora de la isla Lord Howe"],

            "SST"	: [+11,"Hora oficial de las Islas Salomón"],
            "SBT"	: [+11,"Hora oficial de las Islas Salomón"],

            "NST"	: [+12,"Hora oficial de Nueva Zelanda"],
            "ANAT" : [+12, "Hora de Anadyr"],
            "CHAST" : [+12.45, "Hora de la isla Chatham"],
            "TOT"   : [+13, "Hora de Tonga"],
            "LIND"  : [+14, "Hora de las Line Islands"],

            #Negativas
            "AOE"   : [-12, "Hora 'Anywhwere on Earth', usada en el Pacífico y Islas Baker"],
            "MIT"	: [-11,"Hora de las Islas Midway"],
            "NUT"   : [-11, "Hora de las islas Niue"],
            "HST"	: [-10,"Hora oficial de Hawaii"],
            "MART"  : [-9.3, "Hora de las Islas Marquesas"],
            "HDT"   : [-9,"Hora oficial de 'Daylight' de Hawaii. (Marzo a Noviembre)"],
            "AST"	: [-9,"Hora oficial de Alaska"],
            "AKDT"	: [-8,"Hora oficial de 'Daylight' del Alaska. (Marzo a Noviembre)"],
            "PST"	: [-8,"Hora oficial del Pacífico"],
            "PDT"	: [-8,"Hora oficial de 'Daylight' del Pacífico. (Marzo a Noviembre)"],
            "PNT"	: [-7,"Hora oficial de Phoenix"],
            "MST"	: [-7,"Hora oficial de las Montañas Rocosas"],
            "CT"	: [-6,"Hora oficial central (EEUU y Canadá)"], #También referida como CST, pero también China lo usa así que CT
            "EST"	: [-5,"Hora oficial del Este de EE.UU."],
            "IET"	: [-5,"Hora oficial de Indiana (Este)"],
            "CDT"	: [-5,"Hora oficial de 'Daylight' del Centro de EE.UU. (Marzo a Noviembre)"],
            "EDT"	: [-4,"Hora oficial de 'Daylight' del Este de EE.UU. (Marzo a Noviembre)"],
            "PRT"	: [-4,"Hora de Puerto Rico e Islas Vírgenes de EEUU"],
            "CNT"	: [-3.3,"Hora de Terranova (Canadá)"],
            #
            "AGT"	: [-3,"Hora oficial de Argentina"],
            #
            "BET"	: [-3,"Hora de Brasil (Este)"],
            "NDT"   : [-2.3, "Hora de Nwefoundland, Canadá"],
            "WGST"  : [-2, "Hora de verano de Groenlandia occidental"],
            "CAT"	: [-1,"Hora de África central"],
            "CVT"   : [-1, "Hora de Cabo Verde"],}

numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Argento text files have been loaded")