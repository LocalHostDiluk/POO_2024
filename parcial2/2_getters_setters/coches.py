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

#Fin de la clase

#Crear in objeto o instanciar la clase

coche1 = Coches()

#Mostrar los valores inciales del objeto o instancia de la clase
print(f"Marca: {coche1.marca}, color: {coche1.color}, modelo: {coche1.modelo},velocidad: {coche1.velocidad}, caballaje: {coche1.caballaje}, plazas: {coche1.plazas}")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
    coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

coche2 = Coches()
coche2.getVelocidad()
coche2.getCaballaje()
coche2.getColor()
coche2.getMarca()
coche2.getModelo()
coche2.getPlazas()

print(f"Marca: {coche2.marca}, color: {coche2.color}, modelo: {coche2.modelo},velocidad: {coche2.velocidad}, caballaje: {coche2.caballaje}, plazas: {coche2.plazas}")