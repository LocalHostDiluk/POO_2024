from coches import Coches

# print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
# coche1.getInfo()


# print("Objeto 2")
# coche2 = Coches("Azul","Nissan","2020",180,150,6)
# coche2.getInfo()

#print(coche1.publico_atributo) esto no es permitido
print(coche1.getPrivadoAtributo())
coche1.getMetodoPublico()