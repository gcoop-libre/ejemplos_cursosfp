#! -*- coding: utf8 -*-
# Bajar desde http://bottlepy.org

import bottle


@bottle.route('/')
def index():
    return bottle.template('inicio.tpl')

@bottle.route('/saludar/<nombre_del_usuario>', method='GET')
@bottle.route('/saludar', method='POST')
def saludar(nombre_del_usuario=None):

    #Obtenemos el nombre de la persona desde el request
    if nombre_del_usuario == None:
        nombre_del_usuario = bottle.request.forms.get('nombre')

    return bottle.template('saludar.tpl',
                            nombre=nombre_del_usuario,
                            otro_nombre="Jose")


bottle.run(debug=True, reloader=True, host='0.0.0.0')
