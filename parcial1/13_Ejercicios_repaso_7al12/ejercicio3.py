"""
    3.- Crear un programa para comprobar si una lista esta vacia y 
    si esta vacia llenarla con palabras o frases hasta que el 
    usuario asi lo crea conveniente, posteriormente imprimir 
    el contenido de la lista en mayusculas
"""
lista = []
valor = "no"
if len(lista) > 0:
    print("La lista contiene elementos, ¿Desea ingresar más? (S/N)")
    valor = input()
    if valor == "S":
        while valor != "salir":
            valor=input("Ingrese el valor a ingresar o digite 'salir' para terminar: ")
            if valor != "salir":
                lista.append(valor)
        print(lista)
    else:
        print("OK, hasta luego :D")
else:
    while valor != "salir":
            valor=input("Ingrese el valor a ingresar o digite 'salir' para terminar: ")
            if valor != "salir":
                lista.append(valor.upper())
    print(lista)
    print("Hasta luego :D")