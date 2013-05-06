#! -*- coding: utf8 -*-

nombre_archivo = "mis_pruebas.txt"

def guardar_en_archivo(texto):
    """
    Guarda una linea de texto en un archivo, en este caso
    'mis_pruebas.txt'
    """
    archivo = open(nombre_archivo, 'a')
    archivo.write(texto + '\n')
    archivo.close()

def leer_archivo():
    """
    Lee todas las lineas del archivo 'mis_pruebas.txt'
    """
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return lineas

def embellecer_nombre(nombre):
    """convierto el nombre en algo como: '[mi nombre] - '"""
    return  '[%s] - ' % nombre


def cuentas_de_usuario(nombre):
    salida = []
    nombre = embellecer_nombre(nombre)
    for linea in leer_archivo():
        if linea.startswith(nombre):
            #le saco el nombre
            linea = linea.replace(nombre, '')
            salida.append(linea)
    return salida



def hacer_cuenta(texto, nombre=''):
    """
    Hace una cuenta y la guarda en un archivo
    """
    if nombre:
        nombre = embellecer_nombre(nombre)

    guardar_en_archivo('%scuenta: %s' % (nombre, texto))
    # FIXME a veces esto se rompe ver como lo arreglamos :-/
    resultado = eval(texto)
    guardar_en_archivo('%sresultado: %s' % (nombre, resultado))
    return resultado

if __name__ == '__main__':
    guardar_en_archivo('Hola Mundo')
    guardar_en_archivo('Esta es otra linea')
    hacer_cuenta('2 + 2')
    hacer_cuenta('2 + 8', 'horacio')
    print cuentas_de_usuario('horacio')
    print leer_archivo()
