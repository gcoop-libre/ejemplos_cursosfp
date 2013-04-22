
#! -*- coding: utf8 -*- 

# Problemas con if, while, booleanos. 

# Problema 1. Adivinar número 

print "Adivine un número en tres intentos!"

numerodef= 7 
 
intentos= 3

intento= 0 

while intentos > 0 and intentos <= 3:

	intento= intento + 1
	
	print "\nIntento", intento, "de", intentos
	
	tunumero= int (input  ("\nPor favor ingresá un número a continuación: "))
	
	print "\nIngresaste el número: ", tunumero

	if tunumero < numerodef: 
			
		print "\nTu número es menor que el que tenés que adivinar ;)"

	elif tunumero > numerodef:
		
		print "\nTu número es mayor al que tenés que adivinar ;)"
		
	if tunumero == numerodef: 
		
		print "\nAcierto y Ganaste :D"
		
		break 
	
	if intento > 2:
		
		print "\nPerdiste. El número a adivinar era el %d " % numerodef
		
		break
		
