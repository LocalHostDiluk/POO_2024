"""
    2.- Escribir un programa  que añada valores a una lista mientras que su longitud
    sea menor a 120, y luego mostrar la lista: Usar un while y for
"""
lista = []

#Usando while
while len(lista) <=120:
    lista.append(input("Ingresar un valor a la lista: "))

print(lista)

#Usando for
for i in range(1,121):
    lista.append(input("Ingresar un valor: "))

print(lista)