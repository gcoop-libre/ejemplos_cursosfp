#! -*- coding: utf8 -*-

import bottle
import calculador

@bottle.route('/')
def index():
    return bottle.template('calculadora.tpl', cuenta='', total='')


@bottle.route('/hacer_cuenta', method='POST')
def hacer_cuenta():
    """Muestra el resultado y permite hacer una cuenta"""
    cuenta = bottle.request.forms.get('cuenta')
    resultado = calculador.hacer_cuenta(cuenta)
    return bottle.template('calculadora.tpl',
            cuenta=cuenta,
            total=resultado)


if __name__ == '__main__':
    bottle.run(debug=True, reloader=True, host='0.0.0.0')


