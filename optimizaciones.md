# Optimizando nuestros programas

Cuando desarrollamos software es comun encontrarnos con que funciona mas lento 
que lo que esperabamos, o no tiene la performance que queriamos.

El origen de la *falta de performance* puede deberse a varios factores:
 * Errores Algoritmicos: cuando el procedimiento con el que estamos manipulando 
    los datos no está bien definido, o es de una complejidad mayor a la minima 
    posible 
 * Excesivas llamadas a funciones
 * Problemas de Entrada/Salida (I/O)

Algunos de esos factores son salvables, o mejorables, otros, como los problemas
de *IO* son mas complicados, o imposibles de resolver.

Con el tiempo y la experiencia, uno aprende a escribir código que sea mas 
performante, pero la recomendación general, es no hacer optimizaciones 
prematuras. El código mas rápido para resolver un problema, no es por lo 
general, el mas intuitivo, ni el mas legible.

Por otra parte, tampoco es una buena idea empezar a modificar nuestro programa 
si no sabemos **donde** está realmente el cuello de botella. Por suerte, 
python tiene herramientas en la biblioteca estandar muy utiles para realizar 
esas tareas.

# Timeit  

Permite analizar el tiempo de ejecución de una funcion, llamandola varias veces.

Por ejemplo:

```python
import timeit

def contar_letras(palabra):
    contador = 0
    for letra in palabra:
        contador += 1
    return contador

print timeit.timeit(
    "contar_letras('hola mundo')", 
    setup='from __main__ import contar_letras'
    )
```

Nos imprime `1.1090967655181885`
Ese es el tiempo total de llamar *muchas veces* a la función en segundos, por 
defecto timeit ejecuta el codigo un millon de veces, por lo tanto, cada llamada 
a la función demora 1.109 micro segundos (un microsegundo es la millonesima 
parte de un segundo).

En ipython hay un metodo magico mas conveniente:

```
In [15]: %timeit contar_letras('hola mundo')
1000000 loops, best of 3: 1.05 us per loop
```

Es importante notar que el tiempo promedio varia entre ejecuciones.
Para comparar nuestra función con `len('hola mundo')`

```
[16]: %timeit len('hola mundo')
10000000 loops, best of 3: 69.8 ns per loop
```

Se ve claramente que la función contar_letras es mucho mas lenta (15 veces) que 
usar  `len`

# Analizando las llamadas a funciones con profile

Cuando el código que queremos analizar es mas complejo, y tiene muchas funciones
y objetos, es mejor obtener un "perfil" o profile del programa. Un profile es un
reporte que nos muestra cuales son las funciones mas usadas, cuanto se tarda en 
llamarlas, y cuanta memoria utilizan.
Los modulos de python para realizar esas tareas son `profile` (escrito en python)
 y `cProfile` (escrito en C).

#Cache

Una de las técnicas mas utilizadas, para ganar velocidad, sacrificando memoria
es utilizar *caches* dentro de las funciones. Esto no es aplicable a todas las 
funciones, solo a aquellas que dado un conjunto de parametros, siempre devuelven
el mismo valor.

La tecnica consiste en guardar los resultados, para esos parametros, para que 
en el siguiente caso, donde se llame con los mismos parametros, no se tenga que
realizar la computación nuevamente.

Supongamos que tenemos el siguiente escenario:

```
def histograma(texto):
    """Construye un histograma de caracteres de un texto"""
    resultado={}
    for letra in texto.lower():
        if resultado.has_key(letra):
            resultado[letra] += 1
        else:
            resultado[letra] = 1
    
    return resultado 
```

la misma funcion, con un cache, quedaría:

```
cache = {}

def histograma_con_cache(texto):
    """Construye un histograma de caracteres de un texto"""
    if cache.has_key(texto.lower()):
        return cache[texto.lower()]

    resultado={}
    for letra in texto.lower():
        if resultado.has_key(letra):
            resultado[letra] += 1
        else:
            resultado[letra] = 1
    
    cache[texto.lower()] = resultado
    return resultado 
```

A fines de restringir la cantidad de memoria, se podria implementar un registro
de los parametros mas utilizados, y guardar en cache solamente los que se consultan
mas a menudo

 
