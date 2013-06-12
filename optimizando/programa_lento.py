"""Programa para encontrar la suma de todos los numeros capicuas,
menores que 20 millones"""




def es_capicua(numero):
    numero = str(numero)
    print numero
    return numero == numero[::-1]

def calcular_suma_hasta(limite):
    suma = 0
    for numero in xrange(1, limite+1):
        if es_capicua(numero):
            suma += numero
    return suma


print calcular_suma_hasta(20000000)

