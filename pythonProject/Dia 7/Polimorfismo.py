class Vaca:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print (self.nombre + "dice muuu")

class Oveja:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print (self.nombre + "dice beee")


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

"""
animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()
    """
def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)

"""
# Práctica Polimorfismo 1

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
 
for dato in [palabra, lista, tupla]:
    print(len(dato))


# Práctica Polimorfismo 2

class Mago():
    def atacar(self):
        print("Ataque mágico")
 
class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
 
class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
gandalf = Mago()
hawkeye = Arquero()
jack = Samurai()
 
personajes = [hawkeye, gandalf, jack]
 
for personaje in personajes:
    personaje.atacar()


# Práctica Polimorfismo 3

class Mago():
    def defender(self):
        print("Escudo mágico")
 
class Arquero():
    def defender(self):
        print("Esconderse")
 
class Samurai():
    def defender(self):
        print("Bloqueo")
 
def personaje_defender(personaje):
    personaje.defender()




"""