''' Existen varios tipos de operaciones en Python.

El primero, y mas comun es el de la adicion.

'''

x, y, z = 3, 9, '4'
a = 'String'
b = [1, 2, 'lol']


'''
La siguiente linea de codigo imprimira el resultado de sumar x con yield
'''

print(x+y)

''' 
Debemos recordar que es imposible en la gran mayoria de los casos, sumar variables 
de diferentes tipos. En ese caso, poner 

print(x+z)

nos daria un error, puesto que z es del tipo string.



Sin embargo, es posible sumar dos listas
'''

c = [False, '123', 42]

print(b + c)

#la ultima linea seria parecido a b.extend(c)
#sin embargo, b.extend(c) es en realidad b = b + c. Asignandolo a b.

# Tambien podemos sumar strings, esto va a resultar en lo que se llama concatenacion

print(a + a)

''' 
En general, la suma es de las pocas operaciones compartidas por distintos tipos.
El resto de operaciones, que listaremos a seguir son usadas mayoritariamente para
el tipo numerico

Resta (-):

6 - 5

Multiplicacion (*):

12 * 4

Division (/):

4 / 2 

Potenciacion ( ^ ) :

3 ^ 4  (o, equivalentemente, pow(3, 4), o 3 ** 4 )

Resto de division ( % ) :

12 % 7 El resto de la division de 12 entre 7. En este caso es 5

'''

#OPERACIONES BOOLEANAS

'''
 En ciertas ocaciones, necesitamos condicionar nuestro programa a mas 
 de una condicion. Consideremos el siguiente ejemplo:
 
 Python, comprame una empanada si hay plata y si la despensa tiene 
 empanada de pollo.

Como le decimos a python que haga la instruccion?
Usando el operador and ( & )

'''

hay_plata = False
hay_empanada = True

comprar = hay_empanada and hay_plata #equivalentemente, hay_empanada & hay_plata

'''
El operador and recibe DOS booleans, y devuelve UNO. Este resultado sera verdadero
solamente si los dos booleans, sean verdadero, caso contrario devolvera Falso.

Otro operador muy comun es el operador booleano or ( | )

'''

print(hay_empanada or hay_plata) #equivalentemente, hay_empanada | hay_plata

'''
Un ultimo operador, es la negacion. Se pone al inicio del boolean, y lo cambia de sentido

'''

no_hay_plata = not hay_plata #sera Verdadero

'''
Recuerden que al igual que en matematicas, Python va a realizar lo que este dentro
de parentesis en primer lugar.

'''

print (not ( False and (True or True) ) )

#que va a imprimir la consola?
