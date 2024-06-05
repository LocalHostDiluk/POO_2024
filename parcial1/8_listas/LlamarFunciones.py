def buscar(lis, buscarPal):
    for i in lis:
        if buscarPal == i:
            print(f"Si está la palabra {i}. Está en la posición {lis.index(i)}")
            nofind=True
    
    if nofind:
        print("No está la palabra")
    
    return

def RegistrarPeliculas():
   print("\n")
   peliculas=[]
   peliculas.append=input("Ingresa nombre de la pelicula: ").upper()
   return print("Agregado con éxito")