def buscar(lis, buscarPal):
    for i in lis:
        if buscarPal == i:
            print(f"Si está la palabra {i}. Está en la posición {lis.index(i)}")
            nofind=True
    
    if nofind:
        print("No está la palabra")
    
    return

def Agregar():
   print("\n")
   pelicula = input("Ingese la película: ")
   peliculas.append(pelicula)