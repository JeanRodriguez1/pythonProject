"""
Práctica Archivos y Funciones 2
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro,
 y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"


"""

def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")