"""
    Crear un programa que solicite la calificacion de 15 alumnos 
    e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
"""
cont = 0
contn=0
for i in range(1,16):
    c = float(input(f"Ingrese la calificacion del alumno {i}: "))
    if c>=80:
        cont+=1
    else:
        contn+=1
print(f"aprobaron {cont} alumnos y reprobaron {contn}")