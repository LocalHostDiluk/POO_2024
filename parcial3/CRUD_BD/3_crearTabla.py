from conexionBD import *

try:
    micursor = conexion.cursor()
    sql = "CREATE TABLE Clientes2 (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(60), direccion VARCHAR(120), telefono VARCHAR(10))"
    micursor.execute(sql)
except:
    print("Ocurrió un error por favor verifica.")
else:
    print("Tabla creada exitosamente.")