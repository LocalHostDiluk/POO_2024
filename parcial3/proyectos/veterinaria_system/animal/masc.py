from cone import *

class Animales:
    def __init__(self, nombre, raza, edad, id_cliente):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.id_cliente = id_cliente
    
    @staticmethod
    def actualizarHistorial(nwedad, id):
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE animales SET edad = %s WHERE id = %s",(nwedad, id))
            conexion.commit()
            print("\nHistorial actualizado correctamente")
        except Exception as e:
            print("error al actualizar historial: ", e)