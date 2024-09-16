mi_archivo = open('prueba.txt')
"""
una_linea = mi_archivo.readline() # readline para leer solo una linea
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)

"""
todas = mi_archivo.readlines() # .readlines() se carga todo el archivo sobrecargas todo el sistema

todas = todas.pop()

print(todas)


# -----

for l in mi_archivo:
    print("Aqui dice: " + l)


mi_archivo.close()

"""
 # Práctica Abrir y Manipular Archivos 1
archivo = open("texto.txt")
print(archivo.read())

# Práctica Abrir y Manipular Archivos 2
mi_archivo = open("texto.txt")
print(mi_archivo.readline())


# Práctica Abrir y Manipular Archivos 3

archivo = open("texto.txt")
lineas = archivo.readlines()
print(lineas[1])
 
# Alternativa de solución admitida:
# lineas = archivo.readline()
# lineas = archivo.readline()
# print(lineas)



"""

