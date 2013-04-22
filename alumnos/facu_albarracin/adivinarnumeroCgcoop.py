
#! -*- coding: utf8 -*-

# Problemas con if, while, booleanos.

import random

# Problema 3. Adivinar número al azar

print ("Bienvenido! Adivine un número en tres intentos!")

numerodef= random.randint (1, 8)

intentos= 3

intento= 0

# Sentencia break que rompe con la iteracion de un bucle!

while intentos > 0 and intentos <= 3:

	intento= intento + 1

	print ("\nIntento", intento, "de", intentos)

	tunumero= int (input  ("\nPor favor ingresá un número a continuación: "))

	print ("\nIngresaste el número: ", tunumero)

	if tunumero < numerodef:

		print ("\nTu número es menor que el que tenés que adivinar ;)")

	elif tunumero > numerodef:

		print ("\nTu número es mayor al que tenés que adivinar ;)")

	if tunumero == numerodef:

		print ("\nAcierto y Ganaste :D")

		break

	if intento > 2:

		print ("\nPerdiste. El número a adivinar era el %d " % numerodef)

		break

