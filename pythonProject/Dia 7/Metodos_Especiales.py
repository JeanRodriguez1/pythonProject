"""
mi_lista = [1,1,1,1,1,1,1,1]
print(len(mi_lista))

class Objeto:
    pass

mi_objeto = Objeto()
print(len(mi_objeto))
"""

class CD:

    def __init__(self, autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("se elimino")


mi_cd = CD('Pink Floyd', 'The wall', 24)

print (len(mi_cd))

del mi_cd

"""
# Práctica Métodos Especiales 1

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
 
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'
        

# Práctica Métodos Especiales 2

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
 
    def __len__(self):
        return self.cantidad_paginas


# Práctica Métodos Especiales 3

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
 
    def __del__(self):
        print(f'Libro eliminado')

"""