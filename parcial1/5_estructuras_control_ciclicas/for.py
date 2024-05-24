"""
    Este ciclo es un iterativo y se ejecura X veces de acuerdo a los valores numericos enteros establecidos
    
    sintaxis:
        for variable in elemento_iterable(lista, rango, etc):
            ---bloque instrucciones--
"""

#crear programa que imprima 5 veces el caracter arroba (@)

contador = 1
for contador in range(1,6):
    print("@")

#ejemplo 2 crear un programa que imprima los números del 1 al 5, los sume y al final imprima la suma
suma = 0
for numero in range(1,6):
    print(numero)
    suma += numero
print(f"la suma es: {suma}") 

#ejemplo 3 crear un programa qque solicite un numero entero, a continuacion imprima su tabla de multiplicar
num = int(input("Ingrese un número: "))
multi =0
for i in range(1,11):
    multi=i*num
    print(f"{num} x {i} = {multi}")

