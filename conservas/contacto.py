import pickle
import os

class Contacto(object):

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __repr__(self):
        return "<Contacto %s %s>" % (self.nombre, self.apellido)

    def obtener_nombre_y_telefono(self):
        return self.nombre, self.telefono

class Agenda(object):

    def __init__(self, archivo='mis_datos.pickle'):
        self.archivo = archivo
        self.contactos = []
        if os.path.exists(self.archivo):
            self.cargar()

    def buscar_por_nombre(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto

    def guardar(self):
        """Guarde la lista de contactos en el archivo"""
        fh = open(self.archivo, 'w')
        pickle.dump(self.contactos, fh)
        fh.close()

    def cargar(self):
        """Obtiene los contactos desde un archivo"""
        fh = open(self.archivo, 'r')
        self.contactos = pickle.load(fh)
        fh.close()
