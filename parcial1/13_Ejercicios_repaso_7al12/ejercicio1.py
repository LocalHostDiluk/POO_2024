"""
    1.- Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
    a.- Recorrer la lista y mostrarla
    b.- hacer una funcion que recorra la lista de numeros y devuelva un string
    c.- ordenarla y mostrarla
    d.- mostrar su longitud
    e.- buscar algun elemento que el usuario pida por teclado

"""
lista = [1,8,2,7,3,6,4,5]
# a
for i in lista:
    print(i)

#b
def convertir():
    for i in lista:
        i = str(i)
        print(i)
convertir()

#c
lista.sort()
print(lista)

#d
print("La longitud de la lista es: " + str(len(lista)))

#e
try:
    numero = int(input("Ingrese el número a buscar: "))
    nofind = True
    for i in lista:
        if numero == i:
            print(f"El elemento si está en la lista")
            nofind = False
            break
    if nofind:
        print("No está el número")
    
except ValueError:
    print("Ingrese un número (Ej: 5)")