ayudabasica = ("""----ArgentoBot 1.0 6/2021----

+Ping ---> Pong!
+Rick ---> RickRoll
+Fidel ---> Discurso de Fidel Castro, ideal para un canal AFK
+Oraculo ---> Hacele una pregunta y te responde
+ST ---> Calcula impuestos de Steam Argentina (6/2021)
+STI ---> Calcula impuestos sobre Items de Steam (6/2021)
+STS ---> Calcula impuestos con solo enviar un link de Steam (6/2021)
+CC ---> Calculadora Científica
+IMPUFAQ ---> Datos sobre los impuestos y sus cálculos
+CALC ---> Más datos sobre el uso de las calculadoras.
""")

calchelp = (""" ----ArgentoBot 1.0 6/2021----

Las calculadoras disponibles por el momento son:
Impuestos de Steam: +ST + Precio
Items de Steam: +STI + Precio
Impuestos de steam con un link: +STS + Link
Pasar a notación científica: +CC + Número a tratar
Como funcionan los impuestos?: +IMPUFAQ""")

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

faq = ("""----ArgentoBot 1.0 6/2021----

----Impuestos sobre Steam----
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
Información resumida de https://www.mercadopago.com.ar/ayuda/4063

Nota: En caso de que seas responsable inscripto o vivas en Tierra del Fuego, no pagás IVA
""")