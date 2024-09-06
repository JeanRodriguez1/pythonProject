def multiplicar(num1,num2):
    return num1*num2

res = multiplicar(10,2)
print(res)

# Otra forma
def multiplicar1(num1,num2):
    total = num1*num2
    return total

res1 = multiplicar1(10,2)
print(res1)

# Práctica Return 1
def potencia(num1, num2):
    return num1**num2

# Práctica Return 2
dolares = 1200

def usd_a_eur(dolares):
    return dolares * 0.90

# Práctica Return 3
palabra = "Python"

def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra