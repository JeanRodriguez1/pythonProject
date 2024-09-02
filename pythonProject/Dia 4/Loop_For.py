"""  Ejemplo 1
lista = ['a','b','c','d']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

"""
""" Ejemplo 2
lista = ['pablo', 'laura','luis','fede','julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('nombre que no comienzan con l')
"""
""" Ejemplo 3
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)
"""
""" Ejemplo 4 
for letra in 'python':
    print(letra)


for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)
"""
dic = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic.items(): # o valores .values()
    print(item)