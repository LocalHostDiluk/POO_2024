"""
    4.- Crear un script que tenga 4 variables, una lista, una 
    cadena, un entero y un logico,  y que imprima un mensaje 
    de acuerdo al tipo de dato de cada variable. 
    ° Usar funciones

"""

lista=["1231",2131]
cadena="hola"
intero = 100
logico = True

def tipo1():
    print(f"La lista es {lista} y el tipo de dato es {type(lista)}")

def tipo2():
    print(f"El string es {cadena} y el tipo de dato es {type(cadena)}")

def tipo3():
    print(f"El entero es {intero} y el tipo de dato es {type(intero)}")

def tipo4():
    print(f"El logico es {logico} y el tipo de dato es {type(logico)}")

tipo1()
tipo2()
tipo3()
tipo4()