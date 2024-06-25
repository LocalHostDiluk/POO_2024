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

    MÉTODO CONSTRUCTOR: Este método especial se coloca dentro
    de la clase y se utiliza para dar un valor a los atributos
    del objeto al momento de crearlo, es el primer metodo que 
    se ejecuta al crear el objeto y se manda llamar automaticamente 
    al crearlo, es decir este metodo puede recibir parametros al 
    momento de crear el objeto.
    Cuando se crear un metodo constructor se utiliza la funcion init(), 
    para que se llame automáticamente cada vez que se utiliza la clase 
    para crear un nuevo objeto.

"""

#Ejemplo 1 Crear una clase llamada Coches y a partir de la clase 
# crear objetos o instancias con caracteristicas similares

class Coches:

    #Atributos o propiedades
    #Caracteristicas del coche
    #valores inciales es posible declarar al principio de una clase:
    
    #Método constructor
    def __init__(self,color, marca, modelo, velocidad, caballaje, plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas
    
    #En Python el encapsulamiento también se llama visibilidad y por lo general
    #define como será los atributos y métodos, es decir, públicos o privados
    
    #Atributo público
    publico_atributo = "Soy un atributo público"
    #Atributo privado
    __privado_atributo = "Soy un atributo privado"

    #Nota 1: Para utilizar un atributo privado se tendría que hacer dentro
    #de un método que fuera público el método
    def getPrivadoAtributo(self):
        return self.__privado_atributo
    
    #Método privado
    def __getMetdoPrivado(self):
        print("Soy un método privado")
    
    #Nota 2: Para usar un método privado es necesario hacerlo dentro de un
    #método público
    def getMetodoPublico(self):
        self.__getMetdoPrivado

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