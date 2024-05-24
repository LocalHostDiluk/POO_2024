"""
    escribir un programa que muestre
    los cuadrados de los 60 primeros numeros
    naturales
    ***Resolverlo con While y for
"""

i=1
n=1
while i <=60:
    sqr=(n*n)
    print(sqr)
    n+=1
    i+=1

m=1
for a in range(1,61):
    sqr1=(m*m)
    print(sqr1)
    m+=1
    a+=1