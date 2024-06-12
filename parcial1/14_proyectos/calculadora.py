import os
from FuncionCalculadora import *
from math import sqrt

opcion = True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raiz \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    if opcion!="7" and opcion!="5" and opcion!="6":
        n1,n2, ope =solicitarDatos()
        print(getCalculadora(n1,n2,ope))
        esperaTecla()
    elif opcion =="5":
        n = float(input("Ingrese el número para potenciar: "))
        pot=n*n
        print(f"La potencia del número es: {pot}")
        esperaTecla()
    elif opcion == "6":
        n = float(input("Ingrese el número para sacar raiz: "))
        raiz=sqrt(n)
        print(f"La raiz del número es: {raiz}")
        esperaTecla()
    else:
        opcion=False
        print("Hasta luego")