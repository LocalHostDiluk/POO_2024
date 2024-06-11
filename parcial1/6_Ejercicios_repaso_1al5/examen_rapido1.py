sc=0
cont = 0
c= "SI"

while c == "SI":
    nom = input("Ingrese el nombre del alumno: ")
    carr = input("Ingrese la carrera: ")
    c1 = float(input("Ingrese la calificacion parcial 1: "))
    c2 = float(input("Ingrese la calificacion parcial 2: "))
    c3 = float(input("Ingrese la calificacion parcial 3: "))
    cp = float(input("Ingrese la calificacion proyecto final: "))

    pp = (c1+c2+c3)/3
    cf = (pp+cp)/2
    print(f"El promedio de los parciales es: {pp}")
    
    if cf<80 and cp>=50:
        print(f"Presenta extraordinario. La califiación final es {cf}")
        sc+=cf
        cont+=1
    else:
        print(f"La califiación final es: {cf}")
        sc+=cf
        cont+=1
    
    c= input("¿Deseas otra captura: (SI/NO)?")

pcf= sc/cont
print(f"El promedio de califiaciones finales es: {pcf}")
