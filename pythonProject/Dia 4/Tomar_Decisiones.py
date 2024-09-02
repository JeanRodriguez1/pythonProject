"""mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print("No se que animal tienes")"""

# Otras formas

edad = 16
calificacion = 6

if edad < 18 :
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else :
        print('No Aprobado')
else:
    print('Eres un adulto')

"""
Práctica Control de Flujo 1

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
 
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
    
Práctica Control de Flujo 2

edad = 16
tiene_licencia = False
 
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")
    
    
Práctica Control de Flujo 3

habla_ingles = True
sabe_python = False
 
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif (not habla_ingles) and (not sabe_python):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")



"""