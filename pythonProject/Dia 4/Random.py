from random import *

aleatorio = round(uniform(1,5),2)
print(aleatorio)

aleatorio1 = random() #fraccion de un entero
print(aleatorio1)

colores = ['azul','rojo','verde','amarillo']
aleatorio2 = choice(colores)
print(aleatorio2)

aleatorio3 = randint(1,50)
print(aleatorio3)

numeros =list(range(5,50,5))
shuffle(numeros)
print(numeros)