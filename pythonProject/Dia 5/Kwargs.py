# **kwargs = 'key word args' - se puede dar nombres a los argumentos funcionan como diccionarios.

def suma(**kwargs):

    total = 0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total

print(suma(x=3, y=5, z=2))



# Ejemplo 2
def prueba(num1, num2, *args, **kwargs):

    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:
        print(f"arg = {arg}")


    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


prueba(15,50,100,200,300,400,x='uno',y='dos',z='tres')


# Práctica sobre Argumentos Indefinidos (**kwargs) 1
def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

# Práctica sobre Argumentos Indefinidos (**kwargs) 3
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

