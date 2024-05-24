'''
Comentario de varias lineas
Nota: cuando se imprime en pantalla una cadena de caracteres
se trabaja por default con "cadena", es decir python no
puede concatenar otra cosa que no sea un String(str)

'''

texto = "soy una cadena de caracteres"
numero = 23

#concatenar str con str

print("Soy otra cadena y "+texto)

#concatenar str con int

num_str = str(numero)
print("El numero es: "+ num_str)

print("El numero es: "+str(numero))

#concatenar int con str

n1=int('23')
n2= 33

suma = n1 + n2

#print("La suma es: "+suma)
print(f"La suma es: {suma}")

#concatenar float y entero con str

n1 = 23
n2 = 33.0

suma = float(n1) + n2

print(f"la sume es: {suma}")