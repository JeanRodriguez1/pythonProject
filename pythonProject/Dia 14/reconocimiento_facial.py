"""
La practica no la pude realizar ya que no cuento con webcam.
Se tiene que descargar visual estudio con complemento c++.
Biblioteca - cmake.
Biblioteca - dlib
Biblioteca - face-recognition
Biblioteca - numpy
Biblioteca - opencv-python
"""
from cv2 import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)
