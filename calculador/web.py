#! -*- coding: utf8 -*-

import bottle
import calculador

@bottle.route('/')
def index():
    return bottle.template('inicio.tpl')

@bottle.route('/iniciar', method='POST')
def iniciar():
    nombre = bottle.request.forms.get('nombre')
    cuentas = ''.join(calculador.cuentas_de_usuario(nombre))
    return bottle.template('calculadora.tpl',
            nombre=nombre,
            cuentas_anteriores=cuentas,
            cuenta='',
            total='')



@bottle.route('/hacer_cuenta/<nombre>', method='POST')
def hacer_cuenta(nombre):
    """Muestra el resultado y permite hacer una cuenta"""
    cuenta = bottle.request.forms.get('cuenta')
    resultado = calculador.hacer_cuenta(cuenta, nombre)
    cuentas = ''.join(calculador.cuentas_de_usuario(nombre))

    return bottle.template('calculadora.tpl',
            nombre=nombre,
            cuentas_anteriores=cuentas,
            cuenta=cuenta,
            total=resultado)


if __name__ == '__main__':
    bottle.run(debug=True, reloader=True, host='0.0.0.0')


