import zipfile
import shutil
"""
# Ejemplo 1 comprimir

mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()
"""
"""
# Ejemplo 2 descomprimir

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')

zip_abierto.extractall()
"""
# Ejemplo 3 comprimir shutil
carpeta_origen = 'rutadecarpeta'

archivo_destino = 'Todo_Comprimido' # nombre

shutil.make_archive(archivo_destino,'zip',carpeta_origen)

# .unpack_archive es para descomprimir con shutil



