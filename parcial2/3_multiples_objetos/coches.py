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
    
    """
        Crear los métodos setters y getters, estos métodos son importantes
        y necesarios en todas las clases para que el programador interactue
        con los valores de los atributos a través de estos métodos. Digamos
        que es la manera más adecuada y recomendada para solicitar un valor
        (get) y/o ingresar o cambiar uno (set) a un atributo particular de
        la clase a través de un objeto.
        °En teoria se deberia de crear un método Getter y Setter por cada
        atributo que contenga la clase.
        °Los métodos get siempre regresan valor, es decir el valor de la propiedad
        a través del return
        °Por otro lado el método set siempre recibe parametros para cambiar o
        modificar el valor del atributo o propiedad en cuestión.
    """

    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca = marca
    
    def getModelo(self):
        return self.modelo
    def setModelo(self,modelo):
        self.modelo = modelo
    
    def getVelocidad(self):
        return self.velocidad
    def setVelocidad(self,velocidad):
        self.velocidad = velocidad
    
    def getCaballaje(self):
        return self.caballaje
    def setCaballaje(self,caballaje):
        self.caballaje = caballaje
    
    def getPlazas(self):
        return self.plazas
    def setPlazas(self,plazas):
        self.plazas = plazas

    def getInfo(self):
        print(f"Marca: {self.getMarca()}, color: {self.getColor()}, modelo: {self.getModelo()}, velocidad: {self.getVelocidad()}, caballaje: {self.getCaballaje()}, plazas: {self.getPlazas()}")
#Fin de la clase

#Crear un objetos o instanciar la clase

print("Objeto 1")
coche1=Coches()

#Mostrar los valores inicales del objeto o instancia de la clase
# print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")

coche1.getInfo()

#Utilizar los metodos set para cambiar o modificar los valores de los atributos aun cuando tengan un valor o no ... aunque los valores solo cambiaran para el objeto o instancia en cuestion en el momento que otro objeto se crea si se tienen valores iniciales se crea con los valores de los atributos de clase 

#actualizar todas las propiedades de objeto
coche1.setColor("Amarillo")
coche1.setModelo("2020")
coche1.setMarca("Porsche")
coche1.setVelocidad(250)
coche1.setCaballaje(450)
coche1.setPlazas(2)

#Aunque con los atributos se puede mostrar un valor se recomienda que sea a traves de los getters
# print(f"Marca: {coche1.getMarca()} {coche1.getColor()}, numeros de plazas: {coche1.getPlazas()} \nModelo: {coche1.getModelo()} con una velocidad de {coche1.getVelocidad()} Km/h y un potencia de {coche1.getCaballaje()} hp")

coche1.getInfo()

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
    coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

print("Objeto 2")
coche2 = Coches()
coche2.setVelocidad(400)
coche2.setCaballaje(320)
coche2.setColor("Verde")
coche2.setMarca("Audi")
coche2.setModelo("A3")
coche2.setPlazas(4)

coche2.getInfo()
#Para crear multiples objetos

print("Objeto 3")
coche3 = Coches()
coche3.setVelocidad(220)
coche3.setCaballaje(300)
coche3.setColor("Azul metalico")
coche3.setMarca("Lancer")
coche3.setModelo("2024")
coche3.setPlazas(4)

coche3.getInfo()