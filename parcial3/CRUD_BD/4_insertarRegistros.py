from conexionBD import *

try:
    micursor = conexion.cursor()

    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")

    #Forma de insertar registros en la base de datos
    sql1 = "INSERT INTO clientes (id,nombre, direccion, telefono) VALUES (NULL,%s, %s, %s)"
    valores=(nombre, direccion, telefono)
    micursor.execute(sql1, valores)

    #Forma de insertar registros en la base de datos
    sql = "INSERT INTO clientes (nombre, direccion, telefono) VALUES ('{}', '{}', '{}')".format(nombre, direccion, telefono)
    micursor.execute(sql)

    #Sirve para finalizar de manera exitosa la ejecución de la sentencia SQL
    conexion.commit()
except:
    print("Ocurrió un error por favor verifica.")
else:
    print("Registro insertado exitosamente.")