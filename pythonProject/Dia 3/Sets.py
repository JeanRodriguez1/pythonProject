mi_set = set([1,2,3,4,5,2])
print(type(mi_set))
print(mi_set)
print(len(mi_set))
print(2 in mi_set)

#------- OTRA FORMA DE PONER UN SET

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

#------- Union de sets

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#------- metodo agregar
s4 = {1,2,3}
s4.add(4)
print(s4)
#------- metodo eliminar
s5 = {1,2,3}
s5.remove(3)
print(s5)
#------- metodo eliminar
s6 = {1,2,3}
s6.discard(6)
print(s6)
#------- metodo eliminar cualquiera
s7 = {1,2,3}
sorteo = s7.pop()
print(sorteo)
#------- metodo eliminar cualquiera
s8 = {1,2,3}
s8.clear()
print(s8)