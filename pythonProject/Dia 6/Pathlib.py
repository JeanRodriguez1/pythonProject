from pathlib import Path, PureWindowsPath # transformar cualquier ruta en windows

carpeta = Path("C:/Users/DevsJeanPC/OneDrive/One_Devs/Bootcam 2024/Python/pythonProject/Dia 6/prueba.txt")
# print(carpeta.termino)  .read_text() leer el archivo  - .name nombre del archivo - .suffix tipo de archivo - .stem solo nombre

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)


if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")

