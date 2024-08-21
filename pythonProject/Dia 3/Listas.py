
# otra_lista = ['hola',55,6.1] - se pueden poner dif datos.
# resultado = len(mi_lista)  para ver el numero de datos.
# resultado = mi_lista[0:2]
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2

#mi_lista3[0] = 'alfa' # con strings no se puede pero listas si.
#mi_lista3.append('g') #agregar algo a la lista original
eliminando = mi_lista3.pop(0)

print(mi_lista3)
print(eliminando)

# ----------------

lista = ['g','o','b','m','c']
lista.sort() #reordena pero no devuelve nada. y no podemos asignar a una variable.
lista.reverse() # en orden pero al reves
print(lista)


