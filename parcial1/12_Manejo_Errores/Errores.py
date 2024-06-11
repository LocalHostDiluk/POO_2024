"""
    Los errores de exepciones en un lenguaje de programación
    no es otra cosa que los errores en tiempo de ejecución
    Cuando se manejan los errores mediante las excepciones
    en realidad se dice que se evita que se presenten esos
    errores en programa en tiempo de ejecución
"""
import os

#Ejemplo: Se representa un error cuando no es generada una variable

# try:
#     nombre = input("Nombre completo de la persona: ")

#     if len(nombre)>0:
#         nombre_usuario="El nombre de usuario del sistema es: "+nombre

#     print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre")

#Ejemplo 2: Solicitud de un numero y es ingresado otra cosa
os.system("cls")

# try:
#     numero = int(input("Ingresa un número entero: "))
#     if numero > 0:
#         print("Soy un entero positivo")
#     else:
#         print("Soy un numero entero negativo")
# except ValueError:
#     print("No es posible convertir una letra a numero")

#Ejemplo 3: Cuando se generan multiples excepciones

try:
    numero = int(input("Ingresa un número: "))
    print("El cuadrado es: "+str(numero*numero))
except TypeError:
    print("Es necesario convertir el número a entero")
except ValueError:
    print("Introduce un número. No se puede convertir una cadena")
else:
    print("Todo se ejecutó sin errores")
finally:
    print("Ya terminó")