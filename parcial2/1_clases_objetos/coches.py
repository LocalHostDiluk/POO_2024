"""
    Programación orientada a objetos POO o OOP

    CLASES: es como un mokde a traves del cual se
    puede instanciar un objeto dentro de las clases
    se definen atributos (propiedades / caracteristicas)
    y los métodos (funciones o acciones)

    OBJETOS O INSTANCIAS: son parte de una clase los
    objetos o instancias pertenencen a una clase, es
    decir, para intereactuar con la clase o clases y
    hacer uso de los atributos y métodos es necesario 
    crear un objeto u objetos.

"""

#Ejemplo 1 Crear una clase llamada Coches y a partir de la clase 
# crear objetos o instancias con caracteristicas similares

class Coches:

    #Atributos o propiedades
    #Caracteristicas del coche
    #valores inciales es posible declarar al principio de una clase

    marca = "Ferrari"
    color = "rojo"
    modelo = "2010"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Métodos o acciones o funciones que hace un objeto

    def acelerar(self):
        self.velocidad+=1
    
    def frenar(self):
        self.velocidad-=1

#Fin de la clase

#Crear in objeto o instanciar la clase

coche1 = Coches()

#Mostrar los valores inciales del objeto o instancia de la clase
print(f"Marca: {coche1.marca}, color: {coche1.color}, modelo: {coche1.modelo},
    velocidad: {coche1.velocidad}, caballaje: {coche1.caballaje}, plazas: {coche1.plazas}")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
    coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

coche2 = Coches()
coche2.marca = "Porsche"
coche2.color = "Amarillo"
coche2.modelo = "2024"
coche2.plazas = 4
coche2.velocidad = 480
coche2.caballaje = 360

print(f"Marca: {coche2.marca}, color: {coche2.color}, modelo: {coche2.modelo},
    velocidad: {coche2.velocidad}, caballaje: {coche2.caballaje}, plazas: {coche2.plazas}")