"""
    5.- Crear una lista y un diccionario con el contenido de esta tabla: 

    ACCION              TERROR        DEPORTES
    MAXIMA VELOCIDAD    LA MONJA       ESPN
    ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
    RAPIDO Y FURIOSO I  LA MALDICION   ACCION

    imprimir la información
"""

lista = [
    ["Accion","Terror","Deportes"],
    ["MAXIMA VELOCIDAD","LA MONJA","ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MÁS DEPORTE"],
    ["RÁPIDO Y FURIOSO", "LA MALDICION", "ACCIÓN"]
]

for i in lista:
    print(i)

diccionario = {
    "ACCIÓN": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RÁPIDO Y FURIOSO"],
    "TERROR": ["LA MONJA","EL CONJURO","LA MALDICION"],
    "DEPORTES": ["ESPN","MÁS DEPORTE","ACCIÓN"]
}

print(diccionario)