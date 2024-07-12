from conexionBD import *

try:
    micursor = conexion.cursor()
    sql = "SELECT * FROM clientes"
    micursor.execute(sql)
    registros = micursor.fetchall()
except:
    print("Ocurrió un error por favor verifica.")
else:
    for x in registros:
        print(x)