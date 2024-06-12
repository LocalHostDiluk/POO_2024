peliculas = []
def esperaTecla():
    #Muestra mensaje
    print("Presiona una tecla para continuar")
    #Espera a que el usuario presione una tecla
    input()

def buscar():
    print("Las películas registradas son: \n")
    for index, pelicula in enumerate(peliculas, start=1):
        print(f"{index}.- {pelicula}\n")

def Agregar():
    pelicula = input("Ingese la película: ")
    peliculas.append(pelicula)
    print("\n Película agregada con éxito \n")

def eliminar():
    nofind = True
    buscarPel = input("Ingrese la película a borrar: ")
    for i in peliculas:
        if buscarPel == i:
            peliculas.remove(i)
            print(f"Se eliminó con éxito la película {i} \n")
            nofind = False
            break  # Salimos del bucle una vez eliminada la película
    
    if nofind:
        print("No está la película")

def actualizar():
    buscarPel = input("Ingrese la película a actualizar: ")
    for i in peliculas:
        if buscarPel == i:
            nueva = input("Ingrese la nueva pelicula: ")
            peliculas.insert(i.index(),nueva)
            break  # Salimos del bucle una vez actualizada la película

def buscar1():
    buscarPel = input("Ingrese la película a buscar: ")
    for i in peliculas:
        if buscarPel == i:
            print(i)

def vaciar():
    peliculas.clear()