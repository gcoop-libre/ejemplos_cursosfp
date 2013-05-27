



class Contacto(object):

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __repr__(self):
        return "<Contacto %s %s>" % (self.nombre, self.apellido)



class Agenda(object):

    def __init__(self):
        self.contactos = []

    def buscar_por_nombre(self, nombre):
        for contacto in contactos:
            if contacto.nombre == nombre:
                return contacto



contactos = [
        Contacto('Joaquin', 'Sorianello', '123123'),
        Contacto('Alberto', 'Sorianello', '123123'),
        Contacto('Nicolas', 'Sorianello', '123123'),
    ]


def buscar_contacto(nombre):
    for contacto in contactos:
        if contacto.nombre == nombre:
            return contacto


print buscar_contacto('Nicolas').telefono
print buscar_contacto('Foo').telefono

