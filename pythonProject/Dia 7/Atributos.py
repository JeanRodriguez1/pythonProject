class Pajaro:

    alas = True

    def __init__(self, color,especie):  # init es el constructor de la clase
        self.color = color # self representa a la instancia del objeto que se va a crear.
# self.color = es el atributo - = color parametro
        self.especie = especie
"""
    def __init__(self, mi_parametro):  
        self.atributo = mi_parametro
"""

mi_pajaro = Pajaro('negro','Tucan')

print(mi_pajaro.especie)

print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

print (Pajaro.alas)
print (mi_pajaro.alas)

"""
# Práctica Atributos 1

class Casa:
    def __init__(self, color,cantidad_pisos): 
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        
casa_blanca = Casa('blanco','4')

# Práctica Atributos 2

class Cubo:
    caras = 6
    def __init__(self,color):
        self.color = color
        
cubo_rojo = Cubo("rojo")


# Práctica Atributos 3

class Personaje:
    real = False
 
    def __init__(self, especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
        
harry_potter = Personaje('Humano','True','17')




"""