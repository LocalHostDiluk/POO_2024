import mysql.connector

# Conexión a la base de datos
try:
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_python'
    )
except Exception as e:
    print(type(e))
    print(f"Tipo de error: {type(e).__name__}")
    print("Ocurrió un error con el servidor, verifica los datos de conexión.")
else:
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos.")
    else:
        print("Error en la conexión. No fue posible conectarse a la base de datos")

