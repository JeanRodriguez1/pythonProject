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