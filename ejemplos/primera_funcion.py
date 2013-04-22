#! -*- coding: utf8 -*-

def invertir_cadena(cadena):
    lista = list(cadena)
    #invertimos la lista
    lista.reverse()
    resultado = ''.join(lista)
    return resultado

if __name__ == '__main__' or True:
    print "Tests de la funcion"
    a = 'cadena'
    b = invertir_cadena(a)
    if b == 'anedac':
        print "Funcion testeada"
    else:
        print "mmm, algo anda mal... la funcion recibió %s y devolvio %s" %(a, b)

