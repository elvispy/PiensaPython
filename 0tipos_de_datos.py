# En este script vamos a trabajar con los tipos de datos mas usuales en Python

# El primer tipo es el numerico:

x = 7

# Entonces x es guardado en memoria con el valor 7. 
# En python se asignan variables con el operador "="
# El nombre de la variable siempre debe ir a la izquierda. Si pusiesemos 7=x, 
# el interprete de python nos daria error
# tambien podemos asignar mas de una variable en la misma linea

a, b = 4,7

#y asignar una variable en funcion de otra

c = a + b
#cual es el valor de c?
#Tambien podemos reasignar una variable en relacion a ella misma

c = 2*c
x = x-a


#-----------------------------------------

# El segundo tipo es el string

y = "Esta es una linea de texto"

# Entonces estamos pidiendole a Python que memorice que la variable y tiene
# una linea de texto

#-----------------------------------------

# El tercer tipo de dato es el boolean

z = True

tengo_hambre = False

# Estos valores corresponden a los estados "encendido" o "apagado", y son 
# unicamente dos. Veremos que este tipo de datos es importante en ciertas 
#estructuras

#-----------------------------------------

# El ultimo tipo de dato es la lista. Es como una caja de variables, delimitada
# por corchetes y separados por comas

mi_lista = [1, 5, True, "Python 3.7", tengo_hambre]

#Puede contener CUALQUIER objeto (de cualquier tipo, inclusive puede contener listas)

