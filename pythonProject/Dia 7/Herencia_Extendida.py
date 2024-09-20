class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal nacio")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):


    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo # Nuevo atributo


    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")

piolin = Pajaro(3,'amarillo',60)
mi_animal = Animal(5,'negro')


piolin.volar(100)

# HERENCIA MULTIPLES

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print(" jajaja ")
    def hablar(self):
        print("que tal")

class Hijo(Madre,Padre):
    pass

class Nieto (Hijo):
    pass

mi_nieto = Nieto()

print(Nieto.__mro__)

"""
# Práctica Herencia Extendida 1

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")
 
    def reir(self):
        print("Ja ja ja!")
 
class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre, Padre):
    pass

# Práctica Herencia Extendida 2

class Vertebrado():
    vertebrado = True
 
class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")
 
class Reptil(Vertebrado):
    venenoso = True
 
class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")
 
class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")
 
class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass


# Práctica Herencia Extendida 3

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
    
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"









"""