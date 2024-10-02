"""
Medir el tiempo de ejecucion de tu codigo
para saber cual es mas practico.

"""
# lista de numeros de 1 a lo que pase el usuario

import timeit






declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range (1,numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number= 1000000)
print(duracion)

declaracion2 = '''
prueba_while(10)
'''


mi_setup2 = '''
def prueba_while (numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion2, mi_setup2, number= 1000000)
print(duracion2)










""" Solucion 1 
import time
# las dos hacen lo mismo pero en diferente tiempo
inicio = time.time()
prueba_for(10)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(10)
final = time.time()
print(final - inicio)
"""