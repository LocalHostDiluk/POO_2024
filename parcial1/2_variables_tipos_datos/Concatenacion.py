#Formas concatenación en Python

nombre = "Sebastian Lozano"
especialidad = "Área de SW multiplataforma"
carrera = "Ingenieria en Gestión de Software"

#1er formaa
print("\n")

print("Mi nombre es " + nombre + " estoy en la especialidad de " + especialidad + 
      " en la carrera de " + carrera)

print("\n")

#2da forma
print("Mi nombre es ", nombre, " estoy en la especialidad de ", especialidad, 
      " en la carrera de ", carrera)

print("\n")

#3ra forma MÁS COMÚN EN PYTHON
print(f"Mi nombre es {nombre},  estoy en la especialidad de {especialidad}, en la carrera de {carrera}")

print("\n")

#4ta forma
print("Mi nombre es {} estoy en la especialidad de {} en la carrera de {}").format(nombre,especialidad,carrera)

print("\n")

#5ta forma
print('Mi nombre es ' + nombre + 'estoy en la especialidad de ' + especialidad + 
      ' en la carrera de ' + carrera)

print("\n")