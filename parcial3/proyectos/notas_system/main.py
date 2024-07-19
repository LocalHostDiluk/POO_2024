from usuarios import usuario
from notas import nota
import getpass
from funciones import *

def menu_principal():
    while True:
        borrarPantalla()
        print("""
            .::  Menu Principal ::. 
            1.- Registro
            2.- Login
            3.- Salir 
        """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            #Agregar codigo
            obj_usuario=usuario.Usuario(nombre,apellidos,email,password)
            resultado=obj_usuario.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos} se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")    
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Crear objeto para utilizar métodos
            # obj_usuario=usuario.Usuario("","",email,password)
            # registro=obj_usuario.iniciar_sesion()

            #Cuando existe el metodo como estatico
            registro=usuario.Usuario.iniciar_sesion(email,password)
            if  registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t ** Nombre de usuario y/o contraseña incorrectos, intentalo de nuevo ** ...")
                esperarTecla()          
        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print(""" 
            \n \t .::  Menu Notas ::. 
            1.- Crear 
            2.- Mostrar
            3.- Cambiar
            4.- Eliminar
            5.- Salir 
        """)
        opcion = input("\t\t Elige una opción: ")

        if opcion == '1':

            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            obj_nota=nota.Nota(usuario_id,titulo,descripcion)
            resultado=obj_nota.crear()
            if resultado:
                print(f"\n\t Nota creada correctamente ...")
            else:
                print(f"\n\t ** No se pudo crear la nota, intentalo de nuevo ...")
            esperarTecla()
        
        elif opcion == '2':

            borrarPantalla()
            registro=nota.Nota.mostrar(usuario_id)
            if registro:
                print(f"\n \t \t .:: Notas de {nombre} {apellidos} ::. \n")
                num_nota=1
                for x in registro:
                    print(f"\t Número de nota: {num_nota}")
                    print(f"\t ID: {x[0]}")
                    print(f"\t Título: {x[2]}")
                    print(f"\t Descripción: {x[3]}")
                    print(f"\t Fecha: {x[4]}")
                    print("\t ------------------------------")
                    num_nota+=1
                esperarTecla()
            else:
                print(f"\n\t ** No hay notas para mostrar ...")
                esperarTecla()
            #Agregar codigo

        elif opcion == '3':
            
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            
            resultado=nota.Nota.actualizar(id,titulo,descripcion)
            if resultado:
                print("\n \t \t .:: Nota Actualizada ::. \n")
                esperarTecla()
            else:
                print("\n \t \t ** No se pudo actualizar la nota, intentalo de nuevo ...")
                esperarTecla()
        
        elif opcion == '4':
        
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = int(input("\t \t ID de la nota a eliminar: "))
            resultado=nota.Nota.eliminar(id)
            if resultado:
                print("\n \t \t .:: Nota Eliminada ::. \n")
                esperarTecla()
            else:
                print("\n \t \t ** No se pudo eliminar la nota, intentalo de nuevo ...")
                esperarTecla()

        elif opcion == '5':
            break
        else:
        
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()