from conexionBD import *

try:
    micursor = conexion.cursor()
    sql = "UPDATE clientes SET direccion='Col Valle Verde' WHERE id = 2"
    micursor.execute(sql)
    conexion.commit()
except:
    print("Ocurrió un error por favor verifica.")
else:
    print("Registro actualizado exitosamente.")