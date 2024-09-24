def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)



try:
    # Codigo que queremos probar
    suma()
except TypeError:
    # Codigo a ejecutar si no hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    # Codigo a ejecutar si no hay un error
    print("Este no es un numero")
else:
    # Codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    # Codigo a ejecutar de todos modos
    print("Eso fue todo el codigo")

""" # Mas simplificado
def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Este no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Gracias")

pedir_numero()

"""

# Practicas :
"""
# Práctica Manejo de Errores 1

def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")


# Práctica Manejo de Errores 2

def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


# Práctica Manejo de Errores 3

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")








"""