#!-*- coding: utf8 -*-

import calculador

formas_de_salir = ['chau', 'salir', 'exit']

if __name__ == '__main__':
    print 'Bienvenido a la calculadora sencilla'
    print 'Se guardaran sus cuentas en el archivo: "%s"' % calculador.nombre_archivo
    print 'Puede salir escribiendo alguna de las siguientes palabras:'
    print ', '.join(formas_de_salir)
    while True:
        entrada = raw_input('Ingrese una expresion\n+-< ')
        if entrada in formas_de_salir:
            break
        else:
            resultado = calculador.hacer_cuenta(entrada)
            print '|\n+-> %s' % resultado



