from conexionBD import *
import hashlib
import datetime
import funciones

class Usuario:
    def __init__(self, nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos=apellidos
        self.email=email
        self.contrasena = self.hash_password(password)
        # self.contrasena = password

    
    #Funcion para encriptar la contraseña
    def hash_password(self,contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def registrar(self):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values (null,%s,%s,%s,%s,%s)",
                (self.nombre,self.apellidos,self.email,self.contrasena,fecha)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email,contrasena):
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        try:
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return []    
        except:
            return []

    # def iniciar_sesion(self):
    #     contrasena=hashlib.sha256(self.contrasena.encode()).hexdigest()
    #     try:
    #         cursor.execute(
    #             "select * from usuarios where email=%s and password=%s",
    #             (self.email,contrasena)
    #         )
    #         # print(f"email: {self.email} - contrasena: {contrasena}")
    #         usuario=cursor.fetchone()
    #         # print(f"usuario: {usuario}")
    #         # funciones.esperarTecla()
    #         if usuario:
    #             return usuario
    #         else:
    #             # print("entre en el else")
    #             # funciones.esperarTecla()    
    #             return []
    #     except:
    #         #print("entre en la excepcion")
    #         return []