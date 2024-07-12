import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
    )
except:
    print("Error al conectar a la base de datos.")
else:
    
    #Crear un objeto de tipo cursor que permita ejecutar sentencias SQL
    micursor = conexion.cursor()

    sql = "CREATE DATABASE bd_python"
    #micursor.execute("CREATE DATABASE bd_python")

    #Ejecutar la sentencia SQL
    micursor.execute(sql)

    if micursor:
        print("Base de datos creada exitosamente.")

    #Mostrar las bases de datos existentes
    micursor.execute("SHOW DATABASES")
    for x in micursor:
        print(x)
