nombre = input("Hola cual es tu nombre ? ")
ventas = input("Cuanto ganaste el dia de hoy ? ")
total = float(ventas) * 13 / 100
totalred = round(total,2)

print (f"ok {nombre}.  este mes ganaste {totalred}")


#/ Solucion del video

#/ nombre1 = input("Por favor, dime tu nombre: ")
#/ ventas1 = int(input("Diga sus ventas totales del mes: "))
#/ comision = round(ventas1 * 13 / 100,2)
#/ print(f"Hola {nombre1}, tus comisiones de este mes son de ${comision}")

