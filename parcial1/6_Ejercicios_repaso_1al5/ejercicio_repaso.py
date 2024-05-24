"""
    crear un programa que calcule y obtenga
    el total a pagar por un producto determinado. 
    Se deberá solicitar nombre o descripción, codigo, cantidad,
    precio unitario.
    El total a pagar incluye el IVA y el descuento.
    Si se compran de 1 a 5 productos se otorga el 10% de
    descuento, si se compran de 6 a 10 el 15% de descuento y
    si se compran mas de 10 el 20% de descuento
"""
nom = input("Ingrese el nombre o descripción del producto: ")
cod = int(input("Ingrese el código del producto: "))
can = int(input("Ingrese la cantidad: "))
precio = float(input("Ingrese el precio unitario: "))

cost= can*precio
iva = cost*.16
subtotal = cost + iva

if can <=5:
    descuento = .90
elif can >=5 and can <=10:
    descuento = .85
else:
    descuento = .80

total = subtotal*descuento
print(f"El precio final es de {total}")