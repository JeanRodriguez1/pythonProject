""" Ejemplo 1
monedas = 5

while monedas > 0 :
    print(f"Tengo {monedas} monedas")
    monedas -= 1 #monedas - 1
else:
    print("No tengo mas dinero")
"""


""" Ejemplo 2 
respuesta = 's'

while respuesta == 's':
    respuesta = input("quieres seguir ? (s/n) ")
else:
    print("Gracias")
"""
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'a':
        continue
    print(letra)