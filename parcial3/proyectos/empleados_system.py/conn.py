import mysql.connector

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='mi_empresa'
    )
    #Crear un objeto de tipo cursor que tenga un parametro que permita reutilizar el objeto 
    cursor=conexion.cursor(buffered=True)
except:
    print(f"Ocurrio un error con el Sistema por favor verifique ...")

def cerrar_conexion():
    if conexion.is_connected():
        conexion.close()
        print("\n Conexión cerrada")
        print("..:: Gracias por usar el sistema de empleados ::..\n")