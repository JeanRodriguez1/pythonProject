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