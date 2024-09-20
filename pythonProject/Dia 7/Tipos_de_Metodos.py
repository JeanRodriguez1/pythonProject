""" METODOS DE INSTANCIA
class Pajaro:

    alas = True

    def __init__(self, color,especie):
        self.color = color
        self.especie = especie

    def Piar(self):
        print('Pio, mi color es {}'.format(self.color))

    def Volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.Piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")


piolin = Pajaro('amarillo','canario')
piolin.pintar_negro()
piolin.Volar(50)

"""
class Pajaro:

    alas = True

    def __init__(self, color,especie):
        self.color = color
        self.especie = especie

    def Piar(self):
        print('Pio, mi color es {}'.format(self.color))

    def Volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.Piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    # Metodo de clase
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    # Metodo estatico
    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.mirar()
Pajaro.poner_huevos(3)

"""
# Práctica Tipos de Métodos 1

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

# Práctica Tipos de Métodos 2

class Jugador:
    vivo = False
    
    @classmethod
    def revivir(cls):
        cls.vivo = True

# Práctica Tipos de Métodos 3

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
        
    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas-1


"""
