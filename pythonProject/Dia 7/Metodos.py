class Pajaro:

    alas = True

    def __init__(self, color,especie):
        self.color = color
        self.especie = especie

    def Piar(self):
        print('Pio, mi color es {}'.format(self.color))

    def Volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro('amarillo','canario')

piolin.Piar()

"""
# Práctica Métodos 1

class Perro:
    
    def ladrar(self):
        print('Guau!')
        

# Práctica Métodos 2

class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')

merlin = Mago()


# Práctica Métodos 3

class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

"""