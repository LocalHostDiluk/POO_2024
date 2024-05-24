"""
    el ciclo While es una estructura de control que itera o repite
    la ejecución de una serie de instrucciones tantas veces como
    la condición se cumpla 'True'
    
    Sintaxis:
        while condición:
            --bloque código--
"""

#crear programa que imprima 5 veces el caracter arroba (@)
contador = 0
while contador <= 5:
    print("@")
    contador +=1

#ejemplo 2 crear un programa que imprima los números del 1 al 5, los sume y al final imprima la suma
suma = 0
contador=0
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"La suma es: {suma}")

#ejemplo 3 crear un programa qque solicite un numero entero, a continuacion imprima su tabla de multiplicar
num = int(input("Ingrese un número: "))
multi =0
i=1
while i<=10:
    multi=i*num
    print(f"{num} x {i} = {multi}")
    i+=1
