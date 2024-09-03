"""     Ejemplo 1 NO RECOMENDABLE
lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1
"""
lista = ['a','b','c']

for item in enumerate(lista):
    print(item)

# Mas bonito
lista2 = ['a','b','c']

for indice,item2 in enumerate(lista2):
    print(indice,item2)

# Con rango
for indice,item3 in enumerate(range(50,55)):
    print(indice,item3)

# Fuera de loops a tuples
lista4 = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples)

""" PRACTICAS
Práctica Enumerador 1

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
 
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

Práctica Enumerador 2

lista_indices = list(enumerate("Python"))

Práctica Enumerador 3

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
 
for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)






"""