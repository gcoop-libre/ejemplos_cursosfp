#! -*- coding: utf8 -*-

entrada = raw_input("ingrese una cadena de texto de ejemplo: ")

corte = ''
while len(corte) != 1:
    corte = raw_input("Ingrese un caracter a contar: ")

lista_entrada = list(entrada)
palabras =  entrada.split(' ')
cantidad_palabras = len(palabras)

contador = 0
for caracter in lista_entrada:
    if caracter == corte:
        contador += 1

print "Se encontro %d veces el caracter %s" % (contador, corte)
print "La cadena '%s' tiene %d palabras" % (entrada, cantidad_palabras)

