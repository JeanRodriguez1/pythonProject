diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)

res = diccionario['c1']
print(res)

# ---------

cliente = {'nomnre':'jean','apellido':'Rodriguez','peso':88,'talla':1.79}
consulta = (cliente['apellido'])
print(consulta)

# ---------

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
# ---------
dic2 = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic2['c3']['s2'])

dic3 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic3['c2'][1].upper())

# --------- Agregar
dic4 = {1:'a',2:'b'}
print(dic4)
dic4[3] = 'c'
print(dic4)
dic4[2] = 'B'
print(dic4)

print(dic4.keys())
print(dic4.values())
print(dic4.items())