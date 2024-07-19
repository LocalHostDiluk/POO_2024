from main import crear_conexion

class Empleados:
    def __init__(self, nombre, salario,puesto):
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto

    def crear_empleado(nombre, puesto, salario):
        cursor = crear_conexion().conexion.cursor()
        query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores = (nombre, puesto, salario)
        cursor.execute(query, valores)
        crear_conexion().conexion.commit()
        print("Empleado creado exitosamente")
    
    def leer_empleados():
        cursor = crear_conexion().conexion.cursor()
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]} dolares")