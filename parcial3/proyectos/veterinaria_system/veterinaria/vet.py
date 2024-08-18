from persona.person import *
from cita.cit import *
from cone import *
from servicio.serv import *

class Veterinarias:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    @staticmethod
    def agregarCliente(cliente: Cliente):
        try:
            sql = """
            INSERT INTO clientes (nombre, direccion, telefono, tipo)
            VALUES (%s, %s, %s, %s)
            """
            values = (cliente.nombre, cliente.direccion, cliente.telefono, cliente.tipo)
            cursor.execute(sql, values)
            conexion.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")
            cliente_id = cursor.fetchone()[0]
            return cliente_id
        except mysql.connector.IntegrityError as e:
            print(f"Error de integridad: {e}. Es posible que el cliente ya exista.")
            return None
        except mysql.connector.Error as e:
            print(f"Error al insertar cliente: {e}")
            return None
    
    @staticmethod
    def agregarEmpleado(empleado: Empleado):
        try:
            sql = """
                INSERT INTO empleados (nombre, direccion, telefono, puesto, salario)
                VALUES (%s, %s, %s, %s, %s)
            """
            values=(empleado.nombre, empleado.direccion, empleado.telefono, empleado.puesto, empleado.salario)
            cursor.execute(sql, values)
            conexion.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")
            empleado_id = cursor.fetchone()[0]
            return empleado_id
        except mysql.connector.IntegrityError as e:
            print(f"Error de integridad: {e}. Es posible que el empleado ya exista.")
            return None
        except mysql.connector.Error as e:
            print(f"Error al insertar empleado: {e}")
            return None

    @staticmethod
    def programarCita(cita: Citas):
        opcion = Citas.confirmar()
        if opcion == "s":
            try:
                sql = "INSERT INTO citas (id_cliente, id_empleado, id_animal, id_servicio, fecha) VALUES (%s, %s, %s, %s, %s)"
                values=(cita.idCliente,cita.idEmpleado ,cita.idAnimal , cita.idServicio, cita.fecha)
                cursor.execute(sql, values)
                conexion.commit()
                print("\n..:: Cita programada correctamente ::..")
            except mysql.connector.Error as e:
                print(f"Error al programar cita: {e}")
        else:
            print("\n..:: Opción no válida ::..")
    
    @staticmethod
    def agregarVacuna(servicio: Vacunas):
        try:
            sql = """
                INSERT INTO servicios (nombre, descripcion, costo, tipo)
                VALUES (%s, %s, %s, %s)
            """
            values=(servicio.nombre, servicio.descripcion, servicio.costo, servicio.tipo)
            cursor.execute(sql, values)
            conexion.commit()
            print("\n..:: Vacuna añadida correctamente ::..")
        except mysql.connector.Error as e:
            print(f"Error al insertar vacuna: {e}")
    
    def agregarConsulta(servicio: Consultas):
        try:
            sql = """
                INSERT INTO servicios (nombre, descripcion, costo, duracion)
                VALUES (%s, %s, %s, %s)
            """
            values=(servicio.nombre, servicio.descripcion, servicio.costo, servicio.duracion)
            cursor.execute(sql, values)
            conexion.commit()
            print("\n..:: Consulta añadida correctamente ::..")
        except mysql.connector.Error as e:
            print(f"Error al insertar consulta: {e}")