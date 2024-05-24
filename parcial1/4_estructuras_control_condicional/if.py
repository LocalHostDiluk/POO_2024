"""
    existe una estructura de condicion llamada "if"
    la cual evalua una condicion para encontrar el valor "True" o se cumple
    la condicion se ejecuta la linea o lineas de codigo

    Tienes 4 variantes de if
    1. if simple
    2. if compuesto
    3. if anidado
    4. if y elif

"""

#Ejemplo 1 if simple
color = "rojo"
if color == "rojo":
    print("soy rojo")

#Ejemplo 2 if compuesto
if color == "rojo":
    print("soy rojo")
else:
    print("no soy rojo")

#Ejemplo 3 if anidado
if color == "rojo":
    print("soy rojo")
    if color != "rojo":
        print("soy otro color")
else:
    print("no soy rojo")
    if color != "rojo":
        print("soy otro color")

#Ejemplo 4 if y elif
if color == "rojo":
    print("soy rojo")
elif color=="negro":
    print("soy negro")
elif color=="verde":
    print("soy verde")
else:
    print("No soy rojo, verde o negro")
