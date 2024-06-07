peliculas = []
def esperaTecla():
    #Muestra mensaje
    print("Presiona una tecla para continuar")
    #Espera a que el usuario presione una tecla
    input()

def buscar():
    print("Las películas registradas son: \n")
    for i in peliculas:
        print(f"{peliculas.index(i)+1}.- {i}\n")

def Agregar():
    pelicula = input("Ingese la película: ")
    peliculas.append(pelicula)
    print("\n Película agregada con éxito \n")

def eliminar():
    nofind=True
    buscarPel = input("Ingrese la película a borrar: ")
    for i in peliculas:
        if buscarPel == i:
            peliculas.pop(peliculas.index(i))
            print("Se eliminó con éxito la película \n")
            nofind=False
    
    if nofind:
        print("No está la película")