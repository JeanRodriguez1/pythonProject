"""
archivo = open('prueba.txt', 'w')

lista = ['hola','mundo','aqui','estoy']

for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

"""
# -------

archivo = open('prueba.txt', 'a')

archivo.write('bienvenido')

archivo.close()


""" Practicas 
# Práctica Crear y Escribir Archivos 1

archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())


# Práctica Crear y Escribir Archivos 2

archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

# Práctica Crear y Escribir Archivos 3

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
 
registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')
 
registro.close()
registro = open("registro.txt","r")
print(registro.read())





"""