"""
Generadores
"""

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()

print(next(g))
print(next(g))
print("Hola mundo")
print(next(g))


""" Ejemplo
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista


def mi_generador():
    for  x in range(1,5):
        yield x * 10


print(mi_funcion())
print("_____") # salto
print(mi_generador())
print("_____") # salto
g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
"""
"""

# Práctica Generadores 1

def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num
 
generador = secuencia_infinita()


# Práctica Generadores 2

def multiplos_siete():
    num = 1
    while True:
        yield 7*num
        num += 1
 
generador = multiplos_siete()


# Práctica Generadores 3

def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
 
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
 
perder_vida = mensaje()


"""