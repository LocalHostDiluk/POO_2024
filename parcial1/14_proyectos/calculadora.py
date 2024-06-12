import os
from FuncionCalculadora import *

opcion = True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    if opcion!="5":
        n1,n2, ope =solicitarDatos()
        print(getCalculadora(n1,n2,ope))
        esperaTecla()
    else:
        opcion=False
        print("Hasta luego")