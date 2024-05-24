"""
    Solicitar el usuario 2 numeros y
    realizar las operaciones basicas
    de una calculadora:
    +, -, /, *
    Mostrar en pantalla el resultado
"""
n1= float(input("Ingrese el primer número: "))
n2= float(input("Ingrese el segundo número: "))

suma = n1 + n2
resta = n1 - n2
div = n1/n2
mult= n1*n2

print(f"La suma es {suma}")
print(f"La resta es {resta}")
print(f"La división es {div}")
print(f"La multipliación es {mult}")
