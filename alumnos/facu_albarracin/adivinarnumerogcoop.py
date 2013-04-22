#! -*- coding: utf8 -*- 

# Problemas con if, while, booleanos. 

# Problema 1. Adivinar número 

numerodef= 7 

tunumero= int (input ("Por favor ingresá un número a continuación: "))
 	
if tunumero < 0:
	
	print "\nIngresa un numero positivo!"

elif tunumero == numerodef:
	
	print "\nAcierto!"

elif tunumero > 10: 
	
	print "\nNo ingresaste un numero entero!"
		
else:
		
	print "\nUps, ingresaste ", tunumero, "pero el número era ", numerodef
			
