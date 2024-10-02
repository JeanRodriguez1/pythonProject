from collections import Counter, defaultdict, namedtuple

# Ejemplo 1

numeros = [8,7,5,4,3,2,5,7,4,2,1,3,5,6,4,32,2,4,4]
print(Counter(numeros))

# Ejemplo 2

print(Counter('mississippi'))

# Ejemplo 3

frase = ' al pan pan y al vino vino'
print(Counter(frase.split()))

# Ejemplo 4

serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4])
print(serie.most_common()) # () adentro cuantos numeros quiero que salgan.
print(list(serie))

# Ejemplo 5 defaultdict

mi_dic = defaultdict (lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

# Ejemplo 6 namedtuple

Persona = namedtuple('persona', ['nombre','altura','peso'])
ariel = Persona('ariel',1.70,79)
print(ariel.altura) # [] tambien se puede con indice


"""
# Práctica Módulo Collections 1

from collections import Counter
 
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
 
contador = Counter(lista)

# Práctica Módulo Collections 2

from collections import defaultdict
 
mi_diccionario = defaultdict(lambda:"Valor no hallado")
mi_diccionario["edad"] = 44

# Práctica Módulo Collections 3

from collections import deque
 
lista_ciudades= deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])


"""