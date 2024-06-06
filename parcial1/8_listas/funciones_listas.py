paises = ["Mexico", "USA","Brasil","Japon"]
numeros = [23,34,12.56,0.100]
texto = ["Hola",True,23,3.1415]

#Ordenar una lista

# el .sort() sirve para ordenar una lista
print(paises)
paises.sort()
print(paises)

#funciona con listas que mezclan int y float
print(numeros)
numeros.sort()
print(numeros)

#no funciona con una lista mixta
# print(texto)
# texto.sort()
# print(texto)

#añadir elementos. insert inserta en una posicion especifica
print(texto)
texto.insert(len(texto),"True")
print(texto)
texto.insert(len(texto),True)

#append inserta en la ultima posicion de la lista
texto.append(False)
print(texto)

#eliminar elementos
numeros.remove(34)
print(numeros)
numeros.pop(0)
print(numeros)