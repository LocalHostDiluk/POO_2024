from conexionBD import *

try:
    micursor = conexion.cursor()
    sql = "DELETE FROM clientes WHERE id = 1"
    micursor.execute(sql)
    conexion.commit()
except:
    print("Ocurrió un error por favor verifica.")
else:
    print("Registro eliminado exitosamente.")