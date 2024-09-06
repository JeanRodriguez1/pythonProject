
def chequear_3_cifras(lista):


    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])
print(resultado)
print(type(resultado))

#Práctica Funciones Dinámicas 1

lista_numeros1 = [1, -30, 222, -454, 342, 12, 3, 12]

def todos_positivos(lista_numeros1):
    for numero in lista_numeros1:
        if numero < 0:
            return False
        else:
            pass
    return True

#Práctica Funciones Dinámicas 2

lista_numeros = [-1,-100,400,3,3000]

def suma_menores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma

#Práctica Funciones Dinámicas 3
lista_numeros = [11, 30,1, 55, 123, 9000, 34, 123]


def cantidad_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad