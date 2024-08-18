from cone import *

class Servicios:
    def __init__(self, nombre, descripcion, costo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
    
    @staticmethod
    def actualizarCosto(nwCosto, id):
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE servicios SET costo = %s WHERE id = %s",(nwCosto, id))
            conexion.commit()
            print("\nCosto actualizado correctamente")
        except Exception as e:
            print("error al actualizar costo: ", e)

class Vacunas(Servicios):
    def __init__(self, nombre, descripcion, costo, tipo):
        super().__init__(nombre, descripcion, costo)
        self.tipo = tipo

    def administrarVacuna():
        print("Administrando vacuna...")

class Consultas(Servicios):
    def __init__(self, nombre, descripcion, costo, duracion):
        super().__init__(nombre, descripcion, costo)
        self.duracion = duracion

    def realizarConsulta():
        print("Realizando consulta...")