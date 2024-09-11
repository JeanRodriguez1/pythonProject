def suma(a,b):
    return a+b

print(suma(5,6)) # son funciones que limitan argumentos

# Funcion args
def sumapro(*args): # lo importante es el * es buena practica utilizar args
    total = 0

    for arg in args:
        total += arg
    return total # se puede utilizar sum(args) y da el mismo resultado de funcion

print(sumapro(5,6,7,6,8,9)) # son funciones que limitan argumentos




# Práctica sobre Argumentos Indefinidos (*args) 1
def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2

    return suma

# Práctica sobre Argumentos Indefinidos (*args) 2
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)

    return suma

# Práctica sobre Argumentos Indefinidos (*args) 3
def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'