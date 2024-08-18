import conn

class Empleados:
    def __init__(self, nombre, puesto,salario):
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto

    
    def crear_empleado(self):
        try:
            query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
            valores = (self.nombre, self.puesto, self.salario)
            conn.cursor.execute(query, valores)
            conn.conexion.commit()
            print("\n Empleado creado exitosamente")
            return True
        except:
            return False
    
    @staticmethod
    def leer_empleados():
        try:
            cursor = conn.conexion.cursor()
            query = "SELECT * FROM empleados"
            cursor.execute(query)
            resultados = cursor.fetchall()
            for fila in resultados:
                print(f"ID: {fila[0]} \n Nombre: {fila[1]} \n Puesto: {fila[2]}\n Salario: {fila[3]} dolares")
                print("----------------------------------------------------")
        except:
            print("Error al leer empleados")
    
    @staticmethod
    def actualizar_empleado(id, nombre, puesto, salario):
        try:
            query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
            valores = (nombre, puesto, salario, id)
            conn.cursor.execute(query, valores)
            conn.conexion.commit()
            print("Empleado actualizado exitosamente")
        except:
            print("Error al actualizar empleado")
    
    @staticmethod
    def eliminar_empleado(id):
        try:
            query = "DELETE FROM empleados WHERE id = %s"
            valor = (id,)
            conn.cursor.execute(query, valor)
            conn.conexion.commit()
            print("Empleado eliminado exitosamente")
        except:
            print("Error al eliminar empleado")