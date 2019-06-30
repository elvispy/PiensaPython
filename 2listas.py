# En este script vamos a aprender como usar el comando print()
# Sirve para mostrar al usuario ciertos datos

print("Quiero mostrar esto al usuario")

#Por ejemplo, strings. Tambien se pueden mostrar variables:

#x = 7

#print(x)

#Y se pueden combinar ambos metodos

#print("El valor de la variable es: ", x)

#------------------------------------

'''
Pasemos a las listas o vectores. Como vimos son cajas con valores
adentro. Estos valores pueden ser variables de cualquier tipo
'''

#ejemplo = [4, 6, "Java", False, [4, 9], x ]

'''
Es hora de que aprendamos a preguntar a Python que hay en la caja

Para esto debemos entender lo que es el indexado. Las listas son cajas
ordenadas. Eso significa que Python sabe que en la lista "ejemplo"
el numero 4 esta a la izquierda del 6, que el valor "Java" esta
a la derecha del 6, etc. Python lee las listas de IZQUIERDA A DERECHA
por lo tanto, el 4 va primero, el 6 va segundo, "Java" va tercero, etc


x =  [v1  ,  v2  ,  v3  ,  v4  ,  v5  ,  v6]
      ^      ^      ^      ^      ^      ^
      |      |      |      |      |      |
      |      |      |      |      |      |
	  x[0]   x[1]   x[2]   x[3]   x[4]   x[5]
	  
Por razones historicas, las computadoras empiezan a contar desde cero
la forma de preguntar a Python sobre una variable es poniendo el nombre
de la lista, y luego, en corchetes, el valor que se pregunta.


'''

#print(ejemplo[3])

#Que valor va a mostrar la linea de codigo anterior?

'''
Supongamos que nos olvidamos de agregar un valor a la caja.
Podemos agregarlo usando el atributo "append" asi:
'''

#ejemplo.append("IDLE")

'''
 Lo que esta dentro del parentesis se va a agregar dentro
 de la lista, contando como UN solo valor
 
 Una funcion importante es len(). Del ingles "length"
 calcula la cantidad de elementos de una lista
'''

#print(len(ejemplo))

#Que valor va a mostrar al usuario la linea de codigo anterior?

