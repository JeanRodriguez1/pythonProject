#
nombres = ['Ana','Hugo','Valeria']
edades = [55,44,33]
ciudades = ['Lima','Madrid','Mexico']

combinados = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

""" PRACTICAS 

Práctica Zip 1

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
 
for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")
Práctica Zip 2

marcas = ["Nike", "Lenovo", "Nissan"]
productos = ["zapatillas", "notebook", "automóviles"]
 
mi_zip = zip(marcas, productos)
Práctica Zip 3

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
 
numeros = list(zip(espaniol, portugues, ingles))



"""