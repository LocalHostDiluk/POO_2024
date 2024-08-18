import _mysql_connector
from mysql.connector import Error
from empleados import emp
import conn

def esperaTecla():
    input("\nPresiona una tecla para continuar...")

def borrarPantalla():
    print("\033[H\033[J")

def menu():
    conexion = conn.conexion
    if conexion:
        while True:
            borrarPantalla()
            print("\n--- Menú de Opciones ---")
            print("1. Crear empleado")
            print("2. Leer empleados")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                borrarPantalla()
                nombre = input("Nombre: ")
                puesto = input("Puesto: ")
                salario = input("Salario: ")
                new_emp = emp.Empleados(nombre, puesto, salario)
                new_emp.crear_empleado()
                esperaTecla()

            elif opcion == '2':
                borrarPantalla()
                emp.Empleados.leer_empleados()
                esperaTecla()

            elif opcion == '3':
                borrarPantalla()
                emp.Empleados.leer_empleados()
                id = input("\n ID del empleado a actualizar: ")
                nombre = input("Nuevo nombre: ")
                puesto = input("Nuevo puesto: ")
                salario = input("Nuevo salario: ")
                emp.Empleados.actualizar_empleado(id, nombre, puesto, salario)
                esperaTecla()

            elif opcion == '4':
                borrarPantalla()
                emp.Empleados.leer_empleados()
                id = input("\n ID del empleado a eliminar: ")
                emp.Empleados.eliminar_empleado(id)
                esperaTecla()

            elif opcion == '5':
                conn.cerrar_conexion()
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()