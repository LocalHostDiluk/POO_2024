import cone
from veterinaria.vet import *
from persona.person import *
from cita.cit import *

def esperaTecla():
    input("\nPresione una tecla para continuar...")

def borrarPantalla():
    print("\033[H\033[J")


def menu():
    conexion = cone.conexion
    val = True
    if conexion:
        while True:
            borrarPantalla()
            print("""--- ..:: Menú principal ::.. ---\n \n 1. Soy cliente\n 2. Soy empleado\n 3. Añadir cliente\n 4. Añadir empleado\n 5. Salir""")
            opcion = input("\n Ingrese una opción: ")

            if opcion == "1":
                    borrarPantalla()
                    try:
                        print("\n ..:: Inicio de Sesión ::.. ")
                        id=int(input("\n Ingresa tu id de cliente: "))
                        registro= Cliente.iniciarSesion(id)

                        if registro:
                            menuCliente(registro[0],registro[1])
                        else:
                            print(f"\n** ID incorrecto, intentalo de nuevo ** ...")
                            esperaTecla()
                            borrarPantalla()
                    except ValueError:
                        print("\n** Ingresa un número válido ** ...")
                        esperaTecla()

            elif opcion == "2":
                borrarPantalla()
                try:
                    print("\n ..:: Identificarse ::.. ")
                    id=int(input(" \nIngresa tu id de empleado: "))
                    registro = Empleado.iniciarSesion(id)

                    if registro:
                        menuEmpleado(registro[0],registro[1])
                    else:
                        print(f"\n** ID incorrecto, intentalo de nuevo ** ...")
                        esperaTecla()
                        borrarPantalla()
                except ValueError:
                    print("\n** Ingresa un número válido ** ...")
                    esperaTecla()

            elif opcion == "3":
                borrarPantalla()
                nombre = input("Ingrese el nombre del cliente: ")
                direccion = input("Ingrese la dirección del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")
                tipo = input("Ingrese el tipo de cliente: ")
                con = input("\n ¿Estás seguro de agregar este cliente? (s/n): ")
                if con == "s":
                    new_cliente = Cliente(nombre, direccion, telefono, tipo)
                    idNwCliente = Veterinarias.agregarCliente(new_cliente)
                    if idNwCliente:
                        print(f"\nCliente añadido correctamente.\nAquí su ID para iniciar sesión: {idNwCliente}")
                    else:
                        print("\nError al agregar cliente")
                    esperaTecla()

                    cursor = conexion.cursor()
                    cursor.execute("SELECT LAST_INSERT_ID();")
                else:
                    print("\nOperación cancelada")
                    esperaTecla()
                
            elif opcion == "4":
                borrarPantalla()
                nombre = input("Ingrese el nombre del empleado: ")
                direccion = input("Ingrese la dirección del empleado: ")
                telefono = input("Ingrese el teléfono del empleado: ")
                puesto = input("Ingrese el puesto del empleado: ")
                salario = float(input("Ingrese el salario del empleado: "))
                con = input("¿Estás seguro de agregar este empleado? (s/n): ")
                if con == "s":
                    new_emp = Empleado(nombre, direccion, telefono, puesto, salario)
                    idNwEmp = Veterinarias.agregarEmpleado(new_emp)
                    if idNwEmp:
                        print(f"\nEmpleado añadido correctamente.\nAquí su ID para iniciar sesión: {idNwEmp}")
                    else:
                        print("\nError al agregar empleado")
                    esperaTecla()
                else:
                    print("\nOperación cancelada")
                    esperaTecla()

            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("\n Opción inválida")
                esperaTecla()

def menuCliente(id_cliente,nombre):
    while True:
        borrarPantalla()
        print(f"""--- ..:: Menú cliente ::.. ---\n
        \nBienvenido {nombre}\n
        1. Agendar cita
        2. Cancelar cita
        3. Actualizar datos
        4. Añadir animal
        5. Borrar animal
        6. Actualizar historial
        7. Salir
        """)
        op = input("\nIngrese una opción: ")
    
        if op == "1":
            borrarPantalla()
            servicio = input("1. Vacunas\n2. Consultas\n¿Qué servicio deseas agendar?: ")
            if servicio == "1":
                try:
                    cursor = cone.conexion.cursor()
                    cursor.execute("SELECT * FROM servicios WHERE tipo = 'vacuna'")
                    servicios = cursor.fetchall()
                    if servicios:
                        borrarPantalla()
                        print("\nVACUNAS DISPONIBLES\n")
                        for servicio in servicios:
                            print(f"ID: {servicio[0]} - Nombre: {servicio[1]} - Precio: {servicio[3]}")
                            print("-----------------------------------------------------------------\n")
                        id_cliente = id_cliente
                        id_servicio = int(input("\nIngrese el ID de la vacuna que desea agendar: "))

                        borrarPantalla()
                        cursor.execute("SELECT * FROM animales WHERE id_cliente = %s",(id_cliente,))
                        animales = cursor.fetchall()
                        if animales:
                            print("\nANIMALES DISPONIBLES\n")
                            for animal in animales:
                                print(f"ID: {animal[0]} - Nombre: {animal[1]} - Raza: {animal[2]} - Edad: {animal[3]}")
                                print("-----------------------------------------------------------------\n")
                            id_animal = int(input("\nIngrese el ID del animal que desea agendar: "))
                            
                            borrarPantalla()
                            cursor.execute("SELECT * FROM empleados")
                            empleados = cursor.fetchall()
                            if empleados:
                                print("\nEMPLEADOS DISPONIBLES\n")
                                for empleado in empleados:
                                    print(f"ID: {empleado[0]} - Nombre: {empleado[1]} - Puesto: {empleado[4]}")
                                    print("-----------------------------------------------------------------\n")
                                id_empleado = int(input("\nIngrese el ID del empleado que desea agendar: "))
                                fecha = input("\nIngrese la fecha de la cita (YYYY-MM-DD): ")
                                new_cita = Citas(id_cliente, id_empleado, id_animal, id_servicio, fecha)
                                Veterinarias.programarCita(new_cita)
                                esperaTecla()
                            else:
                                print("\nNo hay empleados disponibles\n")
                                esperaTecla()
                        else:
                            print("No cuentas con animales registrados")
                            esperaTecla()
                    else:
                        print("\nNo hay vacunas disponibles\n")
                        esperaTecla()
                except Exception as e:
                    print(f"Hubo un error al obtener las vacunas: {e}")
                    esperaTecla()

            elif servicio == "2":        
                try:
                    cursor = cone.conexion.cursor()
                    cursor.execute("SELECT * FROM servicios WHERE duracion > 0")
                    servicios = cursor.fetchall()
                    if servicios:
                        borrarPantalla()
                        print("\nCONSULTAS DISPONIBLES\n")
                        for servicio in servicios:
                            print(f"ID: {servicio[0]} - Nombre: {servicio[1]} - Precio: {servicio[3]}")
                            print("-----------------------------------------------------------------\n")
                        id_cliente = id_cliente
                        id_servicio = int(input("\nIngrese el ID del servicio que desea agendar: "))

                        borrarPantalla()
                        cursor.execute("SELECT * FROM animales WHERE id_cliente = %s",(id_cliente,))
                        animales = cursor.fetchall()
                        if animales:
                            print("\nANIMALES DISPONIBLES\n")
                            for animal in animales:
                                print(f"ID: {animal[0]} - Nombre: {animal[1]} - Raza: {animal[2]} - Edad: {animal[3]}")
                                print("-----------------------------------------------------------------\n")
                            id_animal = int(input("\nIngrese el ID del animal que desea agendar: "))
                            
                            borrarPantalla()
                            cursor.execute("SELECT * FROM empleados")
                            empleados = cursor.fetchall()
                            if empleados:
                                print("\nEMPLEADOS DISPONIBLES\n")
                                for empleado in empleados:
                                    print(f"ID: {empleado[0]} - Nombre: {empleado[1]} - Puesto: {empleado[4]}")
                                    print("-----------------------------------------------------------------\n")
                                id_empleado = int(input("\nIngrese el ID del empleado que desea agendar: "))
                                fecha = input("\nIngrese la fecha de la cita (YYYY-MM-DD): ")
                                new_cita = Citas(id_cliente, id_empleado, id_animal, id_servicio, fecha)
                                Veterinarias.programarCita(new_cita)
                                esperaTecla()
                            else:
                                print("\nNo hay empleados disponibles\n")
                                esperaTecla()
                        else:
                            print("No cuentas con animales registrados")
                            esperaTecla()
                    else:
                        print("\nNo hay consultas disponibles\n")
                        esperaTecla()
                except Exception as e:
                    print(f"Hubo un error al obtener los servicios: {e}")
                    esperaTecla()

        elif op == "2":
            borrarPantalla()
            print("Cancelar cita")
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT * FROM citas WHERE id_cliente = %s",(id_cliente,))
                citas = cursor.fetchall()
                if citas:
                    for cita in citas:
                        print(f"ID Cita: {cita[0]} - ID Servicio: {cita[4]} - Fecha: {cita[5]}")
                    id = int(input("\nIngrese el ID de la cita que desea cancelar: "))
                    Citas.cancelar(id)
                else:
                    print("No cuentas con citas registradas")
            except Exception as e:
                print(f"Hubo un error al obtener las citas: {e}")
            esperaTecla()

        elif op == "3":
            borrarPantalla()
            print("Actualizar datos")
            nom = input("Ingrese su nuevo nombre: ")
            direccion = input("Ingrese su nueva dirección: ")
            telefono = input("Ingrese su nuevo teléfono: ")
            tipo = input("Ingrese su nuevo tipo: ")
            id = id_cliente
            Cliente.actualizarDatos(nom, direccion, telefono, tipo, id)
            esperaTecla()

        elif op == "4":
            borrarPantalla()
            nom = input("Ingrese el nombre del animal: ")
            raza = input("Ingrese la raza del animal: ")
            edad = int(input("Ingrese la edad del animal: "))
            con = input("¿Estás seguro de agregar este animal? (s/n): ")
            if con == "s":
                new_animal = Animales(nom, raza, edad, id_cliente)
                Cliente.añadirAnimal(new_animal)
                esperaTecla()
            else:
                print("\nOperación cancelada")
                esperaTecla()

        elif op == "5":
            borrarPantalla()
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM animales WHERE id_cliente = %s",(id_cliente,))
                animales = cursor.fetchall()
                if animales:
                    for animal in animales:
                        print(f"ID: {animal[0]} - Nombre: {animal[1]} - Raza: {animal[2]} - Edad: {animal[3]}")
                    id = int(input("\nIngrese el ID del animal que desea borrar: "))
                    Cliente.borrarAnimal(id)
                else:
                    print("No cuentas con animales registrados")
            except Exception as e:
                print(f"Hubo un error al obtener los animales: {e}")
            esperaTecla()

        elif op == "6":
            borrarPantalla()
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT * FROM animales WHERE id_cliente = %s",(id_cliente,))
                animales = cursor.fetchall()
                if animales:
                    for animal in animales:
                        print(f"ID: {animal[0]} - Nombre: {animal[1]} - Raza: {animal[2]} - Edad: {animal[3]}")
                    id = int(input("\nIngrese el ID del animal que desea actualizar: "))
                    nwEdad = int(input("\nIngrese la nueva edad del animal: "))
                    Animales.actualizarHistorial(nwEdad, id)
                else:
                    print("No cuentas con animales registrados")
            except ValueError:
                print("\nIngresa un número válido")
            except Exception as e:
                print(f"Hubo un error al obtener los animales: {e}")
            esperaTecla()

        elif op == "7":
            esperaTecla()
            break            

def menuEmpleado(id_empleado,nombre):
    while True:
        borrarPantalla()
        print(f"""--- ..:: Menú empleado ::.. ---\n
        \nBienvenido {nombre}\n
        1. Atender cita
        2. Actualizar datos
        3. Añadir servicio
        4. actualizar costo de servicio
        5. Salir
        """)
        op = input("\nIngrese una opción: ")

        if op == "1":
            borrarPantalla()
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT * FROM citas")
                citas = cursor.fetchall()
                if citas:
                    for cita in citas:
                        print(f"ID Cita: {cita[0]} - ID Servicio: {cita[4]} - Fecha: {cita[5]}")
                    id = int(input("\nIngrese el ID de la cita que desea atender: "))
                    print("Atendiendo cita...")
                    Empleado.atenderCita(id)
                else:
                    print("No hay citas disponibles")
            except Exception as e:
                print(f"Hubo un error al obtener las citas: {e}")
            esperaTecla()

        elif op == "2":
            borrarPantalla()
            print("Actualizar datos")
            nom = input("Ingrese su nuevo nombre: ")
            direccion = input("Ingrese su nueva dirección: ")
            telefono = input("Ingrese su nuevo teléfono: ")
            puesto = input("Ingrese su nuevo puesto: ")
            salario = float(input("Ingrese su nuevo salario: "))
            Empleado.actualizarDatos(nom, direccion, telefono, puesto, salario, id_empleado)
            esperaTecla()

        elif op == "3":
            borrarPantalla()
            print("¿Qué servicio deseas agregar?")
            dec = input("1. Vacuna\n2. Consulta\n")

            if dec == "1":
                borrarPantalla()
                nom = input("Ingrese el nombre de la vacuna: ")
                descripcion = input("Ingrese la descripción de la vacuna: ")
                costo = float(input("Ingrese el costo de la vacuna: "))
                tipo = input("Ingrese el tipo: ")
                con = input("¿Estás seguro de agregar este servicio? (s/n): ")
                if con == "s":
                    new_serv = Vacunas(nom, descripcion, costo, tipo)
                    Veterinarias.agregarVacuna(new_serv)
                    esperaTecla()
                else:
                    print("\nOperación cancelada")
                    esperaTecla()

            elif dec == "2":
                borrarPantalla()
                nom = input("Ingrese el nombre de la consulta: ")
                descripcion = input("Ingrese la descripción de la consulta: ")
                costo = float(input("Ingrese el costo de la consulta: "))
                duracion = float(input("Ingrese la duración de la consulta (horas): "))
                con = input("¿Estás seguro de agregar este servicio? (s/n): ")
                if con == "s":
                    new_serv = Consultas(nom, descripcion, costo, duracion)
                    Veterinarias.agregarConsulta(new_serv)
                    esperaTecla()
                else:
                    print("\nOperación cancelada")
                    esperaTecla()
        
        elif op == "4":
            borrarPantalla()
            try:
                cursor = cone.conexion.cursor()
                cursor.execute("SELECT * FROM servicios")
                servicios = cursor.fetchall()
                if servicios:
                    for servicio in servicios:
                        print(f"ID: {servicio[0]} - Nombre: {servicio[1]} - Precio: {servicio[3]}")
                    id = int(input("\nIngrese el ID del servicio que desea actualizar: "))
                    nwCosto = float(input("\nIngrese el nuevo costo del servicio: "))
                    Servicios.actualizarCosto(nwCosto, id)
                else:
                    print("No hay servicios disponibles")
            except ValueError:
                print("\nIngresa un número válido")
            except Exception as e:
                print(f"Hubo un error al obtener los servicios: {e}")
            esperaTecla()

        elif op == "5":
            esperaTecla()
            break

if __name__ == "__main__":
    menu()