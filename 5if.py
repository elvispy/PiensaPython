'''
Ahora aprenderemos un poco mas sobre el tipo boolean y una
estructura de datos

A veces queremos que ciertos comandos se realicen solo bajo 
circunstancias. Para esto sirve la estructura if

if boolean:
	 --------------
	|		|
	| Instrucciones |
	|		|
	 ---------------

 Si estas en el colegio, y ves que un incendio
ha empezado, lo primero que debes hacer es alertar a las autoridades
competentes.
'''
hay_fuego = False

if hay_fuego:
	print("ALERTA! Un incendio ha iniciado.")

# La linea de codigo se ejecutara solamente si hay_fuego es True
#-------------------------------------------#
#A veces queremos agregar una estructura else:

hay_empanada_y_pan = True

if hay_empanada_y_pan:
	print("Dame empanada con pan xfa")
else:
	print("Empanada nomas dame")

y=10
if y==1:
        print("El valor de y es 1")
elif y==2:
        print("El valor de y es 2")
elif y==3:
        print("El valor de y es 3")

''' Hay varias formas de generar booleanos para usar en las
estructuras if:

1)Nombrando una variable de tipo bool

2) Usando una expresion logica

Ejemplos de expresiones logicas son

4 > 2 // va a retornar True
0 < 4 // va a retornar True
1 == 3 // va a retornar False
4 != 5 // va a retornar True (pregunta si son diferentes)
hay_fuego != hay_empanada_y_pan // va a retornar True

Mucho cuidado! para preguntarle a Python si dos valores son iguales
se usa el operador "==". Si usamos solo uno, Python creera que 
estamos asignando una variable.	
'''
#Ejemplo:

x = 5

if x == 4:
	print(x)
else: 
	x = x + 1
