from FuncionPeliculas import *
import os

opcion= 1
while opcion != 4:
    os.system("cls")
    print("\n..::: Almacen de pelicuklas :::... \n 1.- Consultar \n 2.- Agregar \n 3.- Eliminar \n 4.- Actualizar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR")
    opcion = input("Elige una opción: ").lower()

    if opcion == "1":
        buscar()
        esperaTecla()
    elif opcion == "2":
        Agregar()
        esperaTecla()
    elif opcion == "3":
        eliminar()
        esperaTecla()
    elif opcion == "4":
        actualizar()
        esperaTecla()
    elif opcion == "5":
        buscar1()
        esperaTecla()
    elif opcion == "6":
        vaciar()
        esperaTecla()
    elif opcion == "7":
        print("Hasta luego :D")
        break
    else:
        print("La opción no es válida. Pruebe con otra.")
        esperaTecla()