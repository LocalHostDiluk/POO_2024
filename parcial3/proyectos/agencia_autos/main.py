from conexionBD import *
from revisiones.revision import Revision
from clientes.clientes import Cliente
from autos.autos import Auto
from funciones import *
from usuarios.users import Usuario
import getpass
import os
os.system("cls")

def iniciarSesion():
    if conexion:
        while True:
            borrarPantalla()
            print("\n  .:: Inicio de sesión ::. ")
            op = input("\n 1. Acceder \n 2. Registrarse \n 3. Salir \n\n Opción: ")

            if op == '1':
                borrarPantalla()
                print("\n  .:: Inicio de sesión ::. ")
                email = input("\n Email: ")
                password = getpass.getpass(" Contraseña: ")
                registro = Usuario.login(email, password)
                if registro:
                    menu_principal(registro[1],registro[2])
                else:
                    print("\n Usuario o contraseña incorrectos. Intenta de nuevo.")
                    esperarTecla()
            elif op == '2':
                borrarPantalla()
                print("\n  .:: Registro de Usuario ::. ")

                nombre = input("\n Nombre: ")
                apellido = input(" Apellido: ")
                email = input(" Email: ")
                password = getpass.getpass(" Contraseña: ")
                obj_usuario = Usuario(nombre, apellido, email, password)
                obj_usuario.registrar()
                esperarTecla()
            elif op == '3':
                print("\n Saliendo del sistema ...")
                esperarTecla()
                break
            else:
                print("Opcion no valida")
                esperarTecla()

def menu_principal(nombre, apellido):
    while True:
        borrarPantalla()
        print(f"""
                \n
.::  Menú Principal ::.

Bievenido {nombre} {apellido}
1.- Gestión de Clientes
2.- Gestión de Autos
3.- Gestión de Revisiones
4.- Salir""")
        opcion = input("\nElige una opción: ")
        
        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_autos()
        elif opcion == '3':
            menu_revisiones()
        elif opcion == '4':
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_clientes():
    while True:
        borrarPantalla()
        print("""
.::  Menú Clientes ::. 
1.- Insertar Cliente
2.- Consultar Clientes
3.- Actualizar Cliente
4.- Eliminar Cliente
5.- Salir""")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            borrarPantalla()
            print(f".:: Insertar Cliente ::. ")
            nif = input("NIF: ")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            ciudad = input("Ciudad: ")
            tel = input("Teléfono: ")
            obj_cliente = Cliente(nif, nombre, direccion, ciudad, tel)
            resultado = obj_cliente.insertar()
            if resultado:
                print(f"\n Cliente registrado con exito ")
            else:
                print(f"\nCliente registrado con exito ")
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()
            registros = Cliente.consultar()
            if registros:
                for fila in registros:
                    print(f"\n \t NIF: {fila[0]}")
                    print(f"\t Nombre: {fila[1]}")
                    print(f"\t Dirección: {fila[2]}")
                    print(f"\t Ciudad: {fila[3]}")
                    print(f"\t Teléfono: {fila[4]}")
                    print("\n------------------------------------")
                esperarTecla()
            else:
                print("\nNo hay Clientes registrados ")
            esperarTecla()
            
        elif opcion == '3':
            borrarPantalla()
            print(f"\n.:: Actualizar Cliente ::. ")
            nif = input("NIF a actualizar: ")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            ciudad = input("Ciudad: ")
            tel = input("Teléfono: ")
            resultado = Cliente.actualizar(nif, nombre, direccion, ciudad, tel)  
            if resultado:
                print(f"\n El Cliente se actualizó con Éxito")
            else:
                print(f"\nNo fue posible actualizar el Cliente ")
            esperarTecla()
            
        elif opcion == '4':
            borrarPantalla()
            print(f"\n .:: Eliminar Cliente ::. ")
            nif = input("NIF a eliminar: ")
            resultado = Cliente.eliminar(nif)
            if resultado:
                print(f"\n El Cliente se eliminó con Éxito ")
            else:
                print(f"\n No fue posible eliminar el Cliente ")
            esperarTecla()
            
        elif opcion == '5':
            break
        else:
            print("\n Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_autos():
    while True:
        borrarPantalla()
        print("""

.::  Menú Autos ::. 
1.- Insertar Auto
2.- Consultar Autos
3.- Actualizar Auto
4.- Eliminar Auto
5.- Salir
                    """)
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            borrarPantalla()
            print(f"\n.:: Insertar Auto ::. ")
            matricula = input("Matrícula: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")
            nif = input("NIF del Cliente: ")
            obj_auto = Auto(matricula, marca, modelo, color, nif)
            resultado = obj_auto.insertar()
            if resultado:
                print(f"\n El Auto se guardó con Éxito ")
            else:
                print(f"\nNo fue posible guardar el Auto ")
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()
            registros = Auto.consultar()
            if registros:
                for fila in registros:
                    print(f"\nMatrícula: {fila[0]}")
                    print(f"Marca: {fila[1]}")
                    print(f"Modelo: {fila[2]}")
                    print(f"Color: {fila[3]}")
                    print(f"NIF del Cliente: {fila[4]}")
                    print("\n------------------------------------")
            else:
                print("\n No hay Autos registrados ")
            esperarTecla()
            
        elif opcion == '3':
            borrarPantalla()
            print(f"\n  .:: Actualizar Auto ::. ")
            matricula = input("Matrícula a actualizar: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            color = input("Color: ")
            nif = input("NIF del Cliente: ")
            resultado = Auto.actualizar(matricula, marca, modelo, color, nif)  
            if resultado:
                print(f"\n.:: El Auto se actualizó con Éxito ::. ")
            else:
                print(f"\nNo fue posible actualizar el Auto, por favor verifique ... ")
            esperarTecla()
            
        elif opcion == '4':
            borrarPantalla()
            print(f"\n  .:: Eliminar Auto ::. ")
            matricula = input("Matrícula a eliminar: ")
            resultado = Auto.eliminar(matricula)
            if resultado:
                print(f"\n.:: El Auto se eliminó con Éxito ::. ")
            else:
                print(f"\nNo fue posible eliminar el Auto, por favor verifique ... ")
            esperarTecla()
            
        elif opcion == '5':
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_revisiones():
    while True:
        borrarPantalla()
        print("""
                    \n  
.::  Menu Revisiones ::. 
1.- Insertar 
2.- Consultar
3.- Actualizar
4.- Eliminar
5.- Salir""")
        opcion = input("\nElige una opción: ")
        
        if opcion == '1' or opcion == 'INSERTAR':
            borrarPantalla()
            print(f"\n  .:: Insertar Revision ::. ")
            no_revision = input("No_Revision: ")
            cambifiltro = input("CambifiltroS/N: ")
            cambioaceite = input("CambioaceiteS/N: ")
            cambiofrenos = input("CambiofrenosS/N: ")
            otros = input("Otros: ")
            matricula = input("Matricula: ")
            obj_revision = Revision(no_revision, cambifiltro, cambioaceite, cambiofrenos, otros, matricula)
            resultado = obj_revision.insertar()
            if resultado:
                print(f"\n.:: La Revision se guardó con Éxito ::. ")
            else:
                print(f"\nNo fue posible guardar la Revision, por favor verifique ... ")
            esperarTecla()

        elif opcion == '2' or opcion == 'CONSULTAR':
            borrarPantalla()
            registros = Revision.consultar()
            if len(registros) > 0:
                for fila in registros:
                    print(f"\n  No_Revision: {fila[0]}")
                    print(f" Cambifiltro: {fila[1]}")
                    print(f" Cambioaceite: {fila[2]}")
                    print(f" Cambiofrenos: {fila[3]}")
                    print(f" Otros: {fila[4]}")
                    print(f" Matricula: {fila[5]}")
            else:
                print("\nNo hay Revisiones registrados... ")
            esperarTecla()
            
        elif opcion == '3' or opcion == 'ACTUALIZAR':
            borrarPantalla()
            print(f"\n  .:: Actualizar Revision ::. ")
            no_revision = input("No_Revision a actualizar: ")
            cambifiltro = input("CambifiltroS/N: ")
            cambioaceite = input("CambioaceiteS/N: ")
            cambiofrenos = input("CambiofrenosS/N: ")
            otros = input("Otros: ")
            matricula = input("Matricula: ")
            resultado = Revision.actualizar(no_revision, cambifiltro, cambioaceite, cambiofrenos, otros, matricula)  
            if resultado:
                print(f"\n.:: La Revision se actualizó con Éxito ::. ")
            else:
                print(f"\nNo fue posible actualizar la Revision, por favor verifique... ")
            esperarTecla()
            
        elif opcion == '4' or opcion == 'ELIMINAR':
            borrarPantalla()
            print(f"\n  .:: Eliminar Revision ::. ")
            no_revision = input("No_Revision a eliminar: ")
            resultado = Revision.eliminar(no_revision)
            if resultado:
                print(f"\n.:: La Revision se eliminó con Éxito ::. ")
            else:
                print(f"\nNo fue posible eliminar la Revision, por favor verifique... ")
            esperarTecla()
            
        elif opcion == '5' or opcion == 'VOLVER':
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == '__main__':
    iniciarSesion()
