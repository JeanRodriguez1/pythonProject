import re

"""
# EJEMPLO 1 
texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"


# palabra = 'ayuda' in texto
# print(palabra)


patron = 'ayuda'

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
"""
"""
# EJEMPLO 2
texto = "llama al 564-525-6588 ya mismo"

patron = re.compile(r'(\d{3})-(\d\d\d)-(\d\d\d\d)') # patron = r'\d{3}-\d\d\d-\d\d\d\d'

resultado = re.search(patron, texto)
print(resultado.group(2))

"""
# comprobar si una clave cumple con condiciones

clave = input("clave: ")

patron = r'\D{1}\w{7}' # e234eqwe

chequear = re.search(patron, clave)

print(chequear)

"""
# Práctica Módulo RE 1

import re
 
import re
 
def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
        
        
# Práctica Módulo RE 2

import re
 
def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")
        
        
# Práctica Módulo RE 3

import re
 
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
"""