from conexionBD import *

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    
    def registrar(self):
        try:
            #Insertar un registro en la tabla usuarios
            cursor.execute(f"INSERT INTO usuarios(nombre, apellido, email, contraseña) VALUES('{self.nombre}', '{self.apellido}', '{self.email}', '{self.password}')")
            conexion.commit()
            print(f"Usuario {self.nombre} {self.apellido} registrado con exito")
        except Exception as e:
            print(f"Ocurrio un error al registrar el usuario {self.nombre} {self.apellido}, por favor verifique ...")
            print(f"Error: {str(e)}")
    
    @staticmethod
    def login(email,contraseña):
        try:
            #Buscar un registro en la tabla usuarios
            cursor.execute(f"SELECT * FROM usuarios WHERE email='{email}' AND contraseña='{contraseña}'")
            usuario = cursor.fetchone()
            if usuario:
                return usuario
            else:
                print(f"Usuario no encontrado")
        except Exception as e:
            print(f"Ocurrio un error al buscar el usuario, por favor verifique ...")
            print(f"Error: {str(e)}")