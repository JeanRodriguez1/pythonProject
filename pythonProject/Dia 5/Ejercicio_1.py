""""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.

Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.

Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.

Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio


"""

def devolver_distintos(a,b,c):

    suma = a+b+c
    lista = [a,b,c]

    # Control de flujo
    if suma > 15:
        return max(lista) # El valor maximo
    elif suma < 10:
        return min(lista) # El valor minimo
    else:
        lista.sort() # El sort() metodo ordena la lista en orden ascendente de forma predeterminada.
        return lista[1]

print(devolver_distintos(3,2,7))