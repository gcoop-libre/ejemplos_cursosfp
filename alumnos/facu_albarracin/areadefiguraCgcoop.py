#! -*- coding: utf8 -*- 

# Problema 2 área de figura gcoop 

# Variable ladoa que toma por defecto el valor 50

ladoa= int (input ("Por favor ingrese el valor del lado: "))

# ** es igual a decir potencia

# Sabemos que la formula del área de un cuadrado es lado al cuadrado es decir: l ** 2

area= ladoa ** 2 

# Sabemos que la formula del perímetro de un cuadrado es la suma de sus lados es decir: lado * 4. Ya que un cuadrado solo tiene 4 lados

perimetro= ladoa * 4 	

# Imprimimos 

print "\nEl área de la figura es de: %d cm2." % area, "\n\nSu perímetro es de: %d cm." % perimetro

