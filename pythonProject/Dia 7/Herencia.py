class Animal:


    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal nacio")


class Pajaro(Animal):
    pass

piolin = Pajaro(2,'amarillo')

print(piolin.color)

"""
# Práctica Herencia 1

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass


# Práctica Herencia 2

class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
class Perro(Mascota):
    pass


# Práctica Herencia 3

class Vehiculo:
     def acelerar(self):
         pass
     def frenar(self):
         pass
    
        
        
class Automovil(Vehiculo):
    pass

"""