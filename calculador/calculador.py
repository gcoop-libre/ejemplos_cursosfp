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

def hacer_cuenta(texto):
    """
    Hace una cuenta y la guarda en un archivo
    """
    guardar_en_archivo('cuenta: %s' % texto)
    resultado = eval(texto)
    guardar_en_archivo('resultado: %s' % resultado)
    return resultado



if __name__ == '__main__':
    guardar_en_archivo('Hola Mundo')
    guardar_en_archivo('Esta es otra linea')
    hacer_cuenta('2 + 2')
    hacer_cuenta('2 + 8')
    print leer_archivo()
