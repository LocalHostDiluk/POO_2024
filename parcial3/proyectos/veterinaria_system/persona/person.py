from cone import *
from animal.masc import *

class Personas:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def actualizarDatos(self, nombre, direccion, telefono):
        pass

class Empleado(Personas):
    def __init__(self, nombre, direccion, telefono, puesto, salario):
        super().__init__(nombre, direccion, telefono)
        self.puesto = puesto
        self.salario = salario

    @staticmethod
    def actualizarDatos(nombre, direccion, telefono, puesto, salario, id):
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE empleados SET nombre = %s, direccion = %s, telefono = %s, puesto = %s, salario = %s WHERE id = %s",
            (nombre, direccion, telefono, puesto, salario, id)
            )
            conexion.commit()
            print("\nDatos actualizados correctamente")
        except:
            print("\nError al actualizar los datos")
    
    @staticmethod
    def iniciarSesion(id):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM empleados WHERE id = %s",(id,))
            usuario = cursor.fetchone()
            if usuario:
                return usuario
            else:
                return []
        except Exception as e:
            print(e)
    
    @staticmethod
    def atenderCita(cita):
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM citas WHERE id = %s",(cita,))
            conexion.commit()
            print("\nCita atendida correctamente")
        except Exception as e:
            print(e)

class Cliente(Personas):
    def __init__(self, nombre, direccion, telefono, tipo):
        super().__init__(nombre, direccion, telefono)
        self.tipo = tipo

    @staticmethod
    def actualizarDatos(nombre, direccion, telefono, tipo, id):
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE clientes SET nombre = %s, direccion = %s, telefono = %s, tipo = %s WHERE id = %s",
            (nombre, direccion, telefono, tipo, id)
            )
            conexion.commit()
            print("\nDatos actualizados correctamente")
        except:
            print("\nError al actualizar los datos")
    
    @staticmethod
    def iniciarSesion(id):
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = %s",(id,))
            usuario = cursor.fetchone()
            if usuario:
                return usuario
            else:
                return []
        except Exception as e:
            print(e)
    
    @staticmethod
    def añadirAnimal(clase: Animales):
        try:
            sql = " INSERT INTO animales (nombre, raza, edad, id_cliente) VALUES (%s, %s, %s, %s) "
            values = (clase.nombre, clase.raza, clase.edad, clase.id_cliente)
            cursor.execute(sql, values)
            conexion.commit()
            print("\nAnimal añadido correctamente")
        except Exception as e:
            print(f"\nError al añadir animal {e}")
    
    @staticmethod
    def borrarAnimal(id):
        try:
            cursor.execute("DELETE FROM animales WHERE id = %s",(id,))
            conexion.commit()
            print("\nAnimal eliminado correctamente")
        except Exception as e:
            print(f"\nError al eliminar animal {e}")