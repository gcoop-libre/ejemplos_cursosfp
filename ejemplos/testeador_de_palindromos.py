#! -*- coding: utf8 -*-

acentos = ['á', 'é', 'í', 'ó', 'ú' ]

entrada = raw_input("Ingrese el palindromo a testear: ")

for letra in acentos:
    if letra in entrada.lower():
        print "Este tester no funciona con acentos :("
        break

entrada_como_lista = list(entrada)

#Doy vuelta la lista
entrada_como_lista.reverse()
pegamento = '' #lo mismo que ""
cadena_dada_vuelta = pegamento.join(entrada_como_lista)

if cadena_dada_vuelta.lower() == entrada.lower():
    print "Viva, encotramos que %s es un palindromo" % entrada
else:
    print "%s no es un palindromo" % entrada
