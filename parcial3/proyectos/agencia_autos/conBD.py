import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user = 'root',
        password = '',
        database = 'bd_agencia_autos'
    )
    cursor = conexion.cursor(buffered=True)
except Exception as e:
    print("Error al conectar a la base de datos: ", e)
