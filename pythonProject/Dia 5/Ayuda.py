dic = {'clave1': 100, 'clave2': 500}

a = dic.popitem() # Tecla control para ver la info de cada elemento con el cursor
print(a)
print(dic)
# Práctica Métodos y Ayuda 1
txt = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
x = txt.lstrip(",:%_#")
print(x)

# Práctica Métodos y Ayuda 2

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

# Práctica Métodos y Ayuda 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)