
""" SIN COMPRENSION DE LISTAS
palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra) # .append para agregar un valor
print(lista)

"""

lista = [letra for letra in 'python']
print(lista)

lista1 = [n for n in range(0,21,2)]
print(lista1)

lista2 = [n / 2 for n in range(0,21,2)]
print(lista2)

lista3 = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]
print(lista3)

pies = (10,20,30,40,50)
metros = [ c / 3.281 for c in pies ]
print(metros)
