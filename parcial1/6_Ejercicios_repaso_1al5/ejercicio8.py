"""
    Hacer un programa que resuelva lo siguiente. 
    ¿Cuanto es el X por ciento de X numero?
"""
x=float(input("Ingrese el numero: "))
y=float(input("Ingrese el porcentaje a calcular: "))
porc= x*(y/100)

print(f"El {y}% de {x} es: {porc}")