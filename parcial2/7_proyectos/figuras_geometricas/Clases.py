from math import *
from os import *

class Figuras:
    def __init__(self,x,y,visible):
        self.x = x
        self.y = y
        self.visible = visible
    
    def getVisible(self):
        return self.visible

    def estaVisible(self):
        return print(f"¿La figura es visible?: {self.getVisible()}")

    def mostrar(self):
        print("Mostrando la figura")
    
    def ocultar(self):
        print("La figura se está ocultando")
    
    def mover(self,int1,int2):
        print(f"La figura se mueve desde {int1} hacia {int2}")
    
    def calcularArea(self):
        print("Por favor crea una figura para calcular el área")

class Rectangulos(Figuras):
    def __init__(self, x, y, visible,alto,ancho):
        super().__init__(x, y, visible)
        self.__alto = alto
        self.__ancho = ancho
    
    def getX(self):
        return self.x
    def setX(self,x):
        self.x = x
    
    def getY(self):
        return self.y
    def setY(self,y):
        self.y = y
    
    def getVisible(self):
        return self.visible
    def setVisible(self,visible):
        self.visible = visible
    
    def getAlto(self):
        return self.__alto
    def setAlto(self,alto):
        self.__alto = alto
    
    def getAncho(self):
        return self.__ancho
    def setAncho(self,ancho):
        self.__ancho = ancho

    def mostrar(self):
        print(f"X: {self.getX()}, Y: {self.getY()}, Visible: {self.getVisible()}, Alto: {self.getAlto()}, Ancho: {self.getAncho()}")    
    def ocultar(self):
        print("La figura se está ocultando")
    
    def CalcularArea(self,alto,ancho):
        area = (float(alto) * float(ancho))
        return print(f"El área del rectangulo es: {area}")

class Circulos(Figuras):
    def __init__(self, x, y, visible,radio):
        super().__init__(x, y, visible)
        self.__radio = radio
    
    def mostrar(self):
        print(f"X: {self.getX()}, Y: {self.getY()}, Visible: {self.getVisible()}, Radio: {self.getRadio()}")
    def ocultar(self):
        print("La figura se está ocultando")

    def getX(self):
        return self.x
    def setX(self,x):
        self.x = x
    
    def getY(self):
        return self.y
    def setY(self,y):
        self.y = y
    
    def getVisible(self):
        return self.visible
    def setVisible(self,visible):
        self.visible = visible
    
    def getRadio(self):
        return self.__radio
    def setRadio(self,radio):
        self.__radio = radio
    
    def CalcularArea(self,radio):
        area = ((radio)^2) * pi
        return print(f"El área del circulo es: {area}")