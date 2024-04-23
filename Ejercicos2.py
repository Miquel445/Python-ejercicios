<<<<<<< HEAD
print("H ola que tal?:")
primo = int(input("Cuantas veces hay que esctibir Cuñao: "))
cunao = 0
while cunao < primo:
   print("Hola Cuñao")
   cunao += 1
print("Eres un pedazo de cuñao \n pedaszo de Cuñao")  

#Cuantas veces tienes que esctibir cuñao
premoh = "CUÑAOOOO"
for I in premoh:
    print (I)


def generaPares(limite):
        num=1

        while num<limite:
            yield num*2

            num=num+1

devuelvePares=generaPares(10)


print(next(devuelvePares))


print("Aquí va a ir mucho más codigo...")

print(next(devuelvePares))

print("Aquí va a ir mucho más codigo...")

print(next(devuelvePares))


def devuelve_ciudades(*ciudades):
     for elemento in ciudades:
          yield elemento


ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Valencia", "Bilvao")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
=======
print("H ola que tal?:")
primo = int(input("Cuantas veces hay que esctibir Cuñao: "))
cunao = 0
while cunao < primo:
   print("Hola Cuñao")
   cunao += 1
print("Eres un pedazo de cuñao \n pedaszo de Cuñao")  

#Cuantas veces tienes que esctibir cuñao
premoh = "CUÑAOOOO"
for I in premoh:
    print (I)
>>>>>>> 3a5549f70bd5f07fd8b60e6a4f40b1346c61c151
