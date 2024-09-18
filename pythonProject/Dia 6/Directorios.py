import os
from pathlib import Path

ruta = os.chdir('otra ruta') # cambiar de directorio.
archivo = open('nombredelarchivo.txt')
print(archivo.read())

# ruta = os.makedirs('ruta\\NUEVACARPETA')
"""
ruta = 'ruta con archvio'
elemento = os.path.dirname(ruta) # nombre de la ruta
                # .split() # te divide la ruta y el nombre del archivo
print(elemento)

"""
# Eliminar directorio con .rmdir('ruta')

"""
otro_archivo = open('url con archivo')
print(otro_archivo.read())


# Abrir archivos en dif sistemas operativos
carpeta = Path('ruta con \ para que lo lea mac y linux') # con Path cualquier os puede entenderlo
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())
"""