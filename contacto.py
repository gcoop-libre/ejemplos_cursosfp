



class Contacto(object):

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __repr__(self):
        return "<Contacto %s %s>" % (self.nombre, self.apellido)

    def obtener_nombre_y_telefono(self):
        return (self.nombre, self.telefono)

class Agenda(object):

    def __init__(self):
        self.contactos = []

    def buscar_por_nombre(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto


agenda = Agenda()

agenda.contactos = [
    Contacto('Joaquin', 'Sorianello', '123123'),
    Contacto('Alberto', 'Sorianello', '123123'),
    Contacto('Nicolas', 'Sorianello', '123123'),
]

agenda.contactos.append(
    Contacto('Sebastian', 'Sorianello', '123123')
    )
#############

ct = agenda.buscar_por_nombre('Sebastian')

nombre, telefono = ct.obtener_nombre_y_telefono()

print nombre
print telefono
