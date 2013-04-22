#! -*- coding: utf8 -*-

mi_numero = 7
es_un_numero = False

while es_un_numero != True:
    numero_usuario = raw_input("Ingresá un numero entre 1 y 10: ")
    # me fijo si es un numero y termino la iteración
    if numero_usuario.isdigit() and 1 <= int(numero_usuario) <= 10 :
        numero_usuario = int(numero_usuario)
        es_un_numero = True
    else:
        print "El valor %s no cumple con los requisitos" % numero_usuario

if mi_numero == numero_usuario:
    print "Acierto!!!"
else:
    print "El número ingresado %s no es igual a %s" % (numero_usuario, mi_numero)
