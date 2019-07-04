# En este script vamos a trabajar con los tipos de datos mas usuales en Python

# El primer tipo es el entero(numerico):

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

#El segundo tipo es el float. Es cualquier numero que es procedida por un
#punto, que es el separador decimal de python

var = 2.1
pi = 3.14159

#el tipo float existe porque a veces necesitamos precision al guardar datos,
#siendo qu eel tipo entero ocupa menos memoria. Mas adelante veremos
#una sutileza del tipo float a tener en cuenta

#-----------------------------------------

# El tercer tipo es el string

y = "Esta es una linea de texto"

# Entonces estamos pidiendole a Python que memorice que la variable y tiene
# una linea de texto

#-----------------------------------------

# El cuarto tipo de dato es el boolean

z = True

tengo_hambre = False

# Estos valores corresponden a los estados "encendido" o "apagado", y son 
# unicamente dos. Veremos que este tipo de datos es importante en ciertas 
#estructuras

#-----------------------------------------

# El ultimo tipo de dato que veremos es la lista. Es como una caja de variables,
# delimitada por corchetes y separados por comas

mi_lista = [1, 5, True, "Python 3.7", tengo_hambre]

#Puede contener CUALQUIER objeto (de cualquier tipo, inclusive puede contener listas)

