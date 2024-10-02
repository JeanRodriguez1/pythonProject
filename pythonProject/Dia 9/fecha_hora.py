from datetime import datetime, date
"""
import datetime

mi_hora = datetime.time(17,30)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.minute)

mi_dia = datetime.date(2025, 10,19)
print(mi_dia) #.years solo a;o
print(mi_dia.today()) # fecha de hoy

"""

# fecha y hora

mi_fecha = datetime(2025,10,19,22,10,15,2500)
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)


#calcular tiempo

nacimiento = date(1997,10,19)
defuncion = date(2095,6,19)

vida = defuncion - nacimiento
print(vida.days)

# dddd

despierta = datetime(2022,10,5,7,30)
duerme =datetime(2022,10,5,23,45)

vigilia = duerme - despierta
print(vigilia)

"""
# Práctica Módulo Datetime 1

from datetime import date
 
mi_fecha = date(1999, 2, 3)

# Práctica Módulo Datetime 2

from datetime import date
 
hoy = date.today()

# Práctica Módulo Datetime 3

from datetime import datetime
 
minutos = datetime.now().minute






"""