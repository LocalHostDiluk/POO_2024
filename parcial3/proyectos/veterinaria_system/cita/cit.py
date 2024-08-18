from cone import *
class Citas:
    def __init__(self, idCliente, idEmpleado,idAnimal, idServicio, fecha):
        self.idAnimal = idAnimal
        self.idCliente = idCliente
        self.idEmpleado = idEmpleado
        self.idServicio = idServicio
        self.fecha = fecha

    @staticmethod
    def confirmar():
        dec = input("\n¿Desea confirmar la cita? (s/n): ")
        return dec

    @staticmethod
    def cancelar(id):
        dec = input("¿Desea cancelar la cita? (s/n): ")
        if dec == "s":
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM citas WHERE id = %s",(id,))
                conexion.commit()
                print("\nCita cancelada correctamente")
            except Exception as e:
                print(e)
        else:
            print("\n..:: Opción cancelada ::..")