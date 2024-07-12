import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_python'
    )
except:
    print("Error al conectar a la base de datos.")

#ALTER TABLE nombre_de_la_tabla AUTO_INCREMENT = nuevo_valor;