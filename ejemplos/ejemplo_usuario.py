
contenedor = []

entrada_usuario = ''

opciones_para_salir = [
    "chau",
    "me fui",
    "cerrar",
    "baja la cortina",
    "apagar",
]


while entrada_usuario not in opciones_para_salir:
    entrada_usuario = raw_input("Decime un palabra 'chau' para salir: ")
    contenedor.append(entrada_usuario)

print "Ingresaste %d palabras y las palabras son:" % len(contenedor)


for elemento in contenedor:
    if elemento == 'chau':
        print "y el ultimo es...."

    print " - %s" % elemento
