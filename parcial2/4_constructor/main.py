from coches import Coches

print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()


print("Objeto 2")
coche2 = Coches("Azul","Nissan","2020",180,150,6)
coche2.getInfo()

print("Objeto 3")
coche3 = Coches("Amarillo","Audi","2024",380,350,2)
coche3.getInfo()
coche3.setColor("Azul metálico")
coche3.getInfo()