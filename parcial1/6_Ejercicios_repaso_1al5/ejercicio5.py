"""
    Hacer un programa que muestre todos los
    numeros entre 2 numeros que diga el usuario
"""
n1= int(input("Ingrese el primer número: "))
n2= int(input("Ingrese el segundo número: "))
s=n1+1
for i in range(n1,n2):
    if s<n2:
        print(s)
        s+=1