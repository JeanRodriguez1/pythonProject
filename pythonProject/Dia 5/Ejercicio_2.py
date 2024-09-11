"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.

Por ejemplo si al invocar esta función pasamos la palabra
"entretenido" , debería devolver ['d','e','i','n','o','r','t']

"""

def letras_unicas(palabra):

    mi_set = set() # set utiliza colecciones de objetos unicos que no se repiten. si se repiten los ignora.

    for letra in palabra:
        mi_set.add(letra) # add agregar

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista

print(letras_unicas("python"))