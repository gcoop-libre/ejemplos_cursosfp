#! -*- coding: utf8 -*-

nombre_archivo = "mis_pruebas.txt"

def guardar_en_archivo(texto):
    archivo = open(nombre_archivo, 'a')
    archivo.write(texto + '\n')
    archivo.close()

def leer_archivo():
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return lineas



if __name__ == '__main__':
    guardar_en_archivo('Hola Mundo')
    guardar_en_archivo('Esta es otra linea')
    print leer_archivo()
