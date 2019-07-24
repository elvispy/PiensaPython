''' Aqui estare poniendo algunos ejercicios sobre listas. 
INSTRUCCIONES:
1) Una (C) al lado del ejercicio
significa que el ejercicio puede hacerse en el Python IDLE, no hace falta crear un script. 
En caso de no poseer la (C), se recomienda hacer el ejercicio en script.
2) Siempre que use la palabra "definir" o alguna conjugacion suya, significa que estoy pidiendo
que el objeto sea guardado en una variable con nombre. Si no te digo como se debe llamar, el nombre queda
a eleccion tuya. 
3) Siempre que use la palabra "imprimir"  o "retornar", o alguna de sus conjugaciones, te estoy pidiendo que, mediante la 
funcion print() le muestres el resultado esperado al usuario.
-----------------------------------
Ejercicio 1 (C):
Dada la siguiente lista:
x = [1, 3, True, [4,3], 6, "String", 6, 4, -1]

 1)Copie la anterior linea en el Python IDLE.
 2) Elimine todos los valores no numericos en la lista, mediante funciones.
 3) Ordene la lista de mayor a menor, e imprima el mayor valor
 4) Agregue todos los valores entre 2 y 21 inclusive
 5) Imprima cuantos seis hay en la lista
 6) Elimine todos los 6, excepto un seis, dejandolo en la lista
 7) Imprima la lista final
 
 ----------------------------------
 Ejercicio 2(C):
 
 Copie la siguiente linea en el python IDLE:
 
 y = list(range(-270,302,4))
 
 Esta variable es una lista. Es un ejemplo de una lista donde no sabemos cuandos 
 elementos posee
 
 1) Calcule la cantidad de elementos de la lista y
 2) Está el valor 0 en esta lista?
 3) Imprima la posicion del valor mas cercano a 100 que haya en la lista
 
 ------------------------------------
 Ejercicio 3:
 
 Defina una lista con 10 elementos (sin ceros)
 
 Guarde en la variable "prod_list" el producto de todos los elementos
 de la lista e imprimalo en consola
 
 ------------------------------------
 Ejercicio 4:
 
 Defina una lista al comienzo del script, unicamente con strings.
 
 El programa debe imprimir la cantidad de elementos de la lista que
 tienen dos o mas caracteres
 
 ----------------------------------------
 Ejercicio 5:
 
 Defina una lista cualquiera al comienzo de un script
 
 El programa debe imprimir la misma lista, pero eliminando valores repetidos.
 
 -----------------------------------------
 Ejercicio 6:
 
 Para este ejercicio, se necesitaran dos listas, definalas al comienzo de un script
 El programa debe retornar un booleano. True en caso de que las listas compartan un 
 elemento en comun, y False caso contrario
 
 Ejemplo: si las listas fuesen [1, "Hola", False] y [[2,3], 1, True], el programa
 debe retornar True, puesto que el elemento "1" esta en ambas listas
 
 Pero si las listas fuesen [1, "Hola", False] y [[2,3], "1", True], el programa debe
 retornar False
 
 -----------------------------------------
 Ejercicio 7:
 
 Defina una lista al comienzo del script. La lista debe contener solo numeros
 
 El programa debe imprimir otra lista, igual a la original pero todos los numeros
 pares han sido eliminados
 
 Ej: [1, 2, 3, 4, 5, 5, 6, 6] ---->  [1, 3, 5, 5]
 
 -----------------------------------------
 
 Ejercicio 8
 
 Hallar la suma de todos los numeros que son multiplos de 3 o 5 que sean menores a 1000
 
 -----------------------------------------
 
 Ejercicio 9
 
 La secuencia de Fibonacci es una lista de numeros que empieza con un uno, sigue un dos
 y a partir de ahi, el siguiente numero se obtiene a partir de sumar los ultimos dos numeros
 de la lista. Por ejemplo la lista inicia con 
 
 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
 
 Guardar en una lista los primeros 100 numeros de Fibbonacci, y sumar aquellos que esten en
 posiciones pares.
 
 ------------------------------------------
 
 Ejercicio 10
 
 Haga que el usuario ingrese un valor en el Python Shell, con la siguiente linea
 de codgo (escrita en tu script):
 
 valor = input("Ingrese un string: ")
 
 Entonces Python guardara lo que el usuario escriba, en una variable llamada "valor", de tipo string
 Cree e imprima una lista donde se almacenen todos los caracteres usados, en orden alfabetico, 
 sin repeticion. 
 
 Ejemplo: Si el usuario ingresa "curso de python en piensa", el resultado debe ser
 [' ', 'a', 'c', 'd', 'e', 'h', 'i', 'n', 'o', 'p', 'r', 's', 't', 'u', 'y']
 
 --------------------------------------------
 
 Ejercicio 11
 
 Dada una lista definida al comienzo del script, imprimir un boolean al usuario
 True si es que la lista contiene dos terminos iguales consecutivos, 
 False si no es el caso.
 
 Ejemplo: si la lista fuese [1, 2, 3, 4, 4], debe imprmir True
 Pero si la lista fuese  [1, 2, 3, 4, 3, 4] debe imprimir False.
 
 ------------------------------------------------
 
 Ejercicio 12
 
 Imprima la suma de todos los numeros primos menores a 1000.
 Un numero es un numero primo posee solo dos divisores.
 4 no es primo, pues 1, 2 y 4 lo dividen, es decir, posee 3 divisores.
 
 
 -------------------------------------------------
 
 Ejercicio 13
 
 Defina dos listas al inicio del script, que representan fechas
 x = [3, 5, 2014] (3 de mayo de 2014)
 y = [4, 2, 2011] ( 4 de febrero de 2011)
 
 Imprima la diferencia en dias entre las dos fechas (en el ejemplo, debe salir 1184)
 
 -------------------------------------------------
 
 Ejercicio 14 (C)
 
 Copie la siguiente linea en el comienzo del script.
 
 x = [68, 26, 54, 80, 91, 40, 1, 80, 72, 0, 10, 48, 23, 87, 22, 84, 93, 32, 9, 37, 94, 96, 45, 96, 50, 72, 57, 40, 48, 27, 5, 89, 38, 72, 29, 83, 42, 16, 93, 10, 99, 42, 41, 52, 69, 75, 22, 86, 81, 80, 84, 93, 68, 31, 17, 17, 74, 49, 29, 24, 8, 53, 61, 94, 95, 63, 5, 3, 23, 3, 25, 4, 89, 85, 54, 82, 0, 21, 53, 6, 77, 36, 78, 34, 26, 32, 56, 67, 89, 88, 41, 32, 49, 7, 97, 91, 93, 34, 48, 36, 20, 81, 17, 35, 45, 33, 14, 63, 93, 10, 7, 91, 27, 7, 27, 44, 7, 56, 99, 98, 83, 43, 6, 59, 47, 51, 66, 24, 71, 6, 7, 93, 44, 9, 93, 86, 67, 73, 78, 22, 25, 57, 76, 85, 41, 54, 21, 75, 4, 18, 56, 85, 25, 46, 10, 7, 66, 75, 51, 11, 87, 8, 32, 50, 96, 28, 15, 30, 6, 44, 40, 94, 66, 28, 24, 76, 20, 76, 0, 37, 9, 57, 88, 86, 86, 58, 86, 57, 10, 69, 0, 59, 9, 28, 36, 89, 33, 64, 25, 14, 63, 31, 41, 76, 91, 77, 5, 21, 31, 74, 3, 43, 55, 22, 80, 21, 82, 78, 4, 71, 47, 56, 35, 17, 29, 51, 63, 55, 32, 64, 73, 67, 1, 87, 7, 44, 19, 68, 92, 6, 78, 13, 43, 79, 32, 75, 48, 34, 13, 16, 20, 7, 85, 49, 69, 95, 7, 79, 30, 80, 33, 17, 7, 3, 47, 89, 33, 76, 64, 10, 91, 63, 26, 11, 3, 54, 22, 19, 3, 15, 74, 9, 44, 36, 97, 48, 17, 30, 39, 56, 86, 91, 8, 27, 24, 81, 59, 69, 33, 47, 14, 90, 68, 17, 24, 39, 72, 18, 80, 4, 74, 91, 77, 90, 46, 51, 36, 70, 14, 27, 68, 57, 94, 17, 93, 20, 38, 48, 26, 35, 13, 30, 77, 43, 95, 100, 14, 18, 98, 85, 22, 80, 24, 61, 9, 15, 47, 47, 14, 30, 36, 60, 73, 59, 17, 57, 5, 72, 14, 7, 0, 74, 23, 39, 25, 62, 83, 35, 75, 93, 37, 71, 68, 54, 79, 75, 72, 60, 97, 3, 59, 76, 38, 1, 95, 9, 50, 76, 37, 6, 23, 10, 71, 44, 32, 4, 73, 7, 79, 38, 57, 46, 32, 36, 79, 11, 69, 96, 21, 86, 1, 28, 53, 26, 5, 11, 10, 70, 40, 22, 74, 38, 55, 36, 49, 45, 90, 51, 44, 100, 55, 63, 31, 94, 19, 17, 95, 7, 22, 68, 49, 1, 13, 0, 94, 28, 71, 41, 13, 7, 58, 51, 51, 77, 26, 47, 22, 75, 11, 17, 90, 100, 63, 84, 93, 32, 46, 21, 20, 64, 38, 77, 79, 15, 20, 25, 23, 87, 32, 54, 90, 90, 49, 46, 23, 81, 56, 14, 15, 6, 38, 63, 46, 21, 90, 58, 52, 94, 8, 37, 31, 79, 26, 30, 26, 99, 20, 50, 60, 56, 15, 49, 55, 33, 79, 42, 47, 42, 16, 52, 1, 28, 17, 14, 32, 27, 53, 55, 7, 27, 36, 29, 33, 14, 0, 49, 16, 26, 80, 49, 89, 63, 23, 21, 42, 93, 39, 39, 31, 60, 47, 0, 23, 51, 73, 14, 75, 63, 31, 7, 7, 82, 29, 68, 20, 19, 32, 6, 59, 42, 32, 53, 97, 57, 80, 17, 55, 80, 64, 72, 29, 73, 57, 51, 39, 57, 81, 87, 66, 55, 66, 5, 94, 79, 87, 69, 18, 17, 23, 90, 84, 37, 36, 31, 17, 97, 7, 7, 59, 27, 59, 51, 14, 54, 85, 14, 65, 60, 70, 73, 5, 36, 27, 33, 33, 37, 88, 35, 38, 4, 14, 39, 87, 15, 91, 43, 93, 90, 71, 7, 87, 82, 56, 87, 86, 31, 95, 53, 55, 33, 22, 29, 15, 63, 13, 24, 66, 39, 95, 83, 84, 63, 96, 75, 6, 62, 85, 0, 34, 83, 51, 57, 43, 66, 55, 89, 8, 97, 100, 85, 9, 27, 5, 9, 13, 40, 49, 15, 88, 43, 0, 15, 83, 6, 40, 49, 83, 24, 0, 61, 51, 14, 64, 74, 85, 73, 13, 80, 50, 58, 83, 78, 46, 47, 76, 19, 10, 30, 99, 20, 78, 19, 60, 63, 85, 32, 69, 40, 7, 78, 65, 58, 74, 78, 84, 77, 81, 74, 4, 100, 36, 65, 100, 7, 61, 11, 96, 43, 53, 97, 0, 89, 20, 80, 90, 55, 19, 58, 76, 9, 77, 74, 41, 61, 90, 1, 76, 98, 96, 17, 30, 60, 34, 43, 45, 96, 67, 82, 10, 74, 18, 97, 59, 89, 30, 94, 76, 94, 97, 48, 95, 28, 56, 9, 36, 86, 86, 55, 71, 28, 6, 58, 23, 60, 81, 100, 37, 69, 9, 76, 9, 9, 69, 64, 98, 21, 39, 66, 69, 23, 79, 89, 65, 40, 98, 44, 44, 82, 22, 59, 10, 11, 97, 62, 17, 98, 22, 61, 87, 61, 1, 86, 88, 34, 34, 6, 95, 54, 59, 83, 87, 21, 88, 80, 89, 11, 39, 90, 84, 40, 49, 44, 86, 63, 60, 43, 11, 19, 92, 45, 49, 73, 55, 100, 53, 33, 82, 32, 31, 24, 59, 49, 89, 88, 61, 13, 48, 5, 33, 32, 92, 80, 79, 33, 92, 52, 80, 14, 44, 74, 94, 70, 94, 23, 60, 45, 65, 89, 47, 82, 77, 65, 24, 67, 11, 97, 45, 24, 69, 30, 16, 60, 53, 81, 22, 33, 26, 70, 29, 85, 84, 19, 61, 0, 0, 60, 55, 3, 56, 58, 10, 83, 27, 75, 34, 4, 52, 58, 6, 7, 28, 89, 23, 79, 47, 35, 72, 98, 6, 38, 11, 91, 16, 99, 8, 90, 85, 68, 17, 4, 47, 33, 82, 89, 17, 60, 26, 46, 56, 52, 89, 24, 79, 24, 19, 6, 56, 7, 66, 80, 75, 74, 82, 84, 91, 11, 14, 22, 56, 5]
 
 Halle la media, mediana y moda del conjunto de datos
 Si no sabes lo que es media, mediana o moda, puedes acceder al siguiente link:
 https://es.khanacademy.org/math/probability/data-distributions-a1/summarizing-center-distributions/v/statistics-intro-mean-median-and-mode
 
 ---------------------------------------------------
 
 Ejercicio 15
 
 Es hora de jugar Tic Tac Toe. La primera linea del script debe ser una lista definida de la siguiente manera:
 
 tablero = ["XOX", "..X", "OOX"]
 
 El cual representa el tablero. La lista debe contener tres strings de 3 caracteres cada uno. representando
 la fila del tablero en el cual se esta jugando. Por ejemplo, la lista de arriba representa el siguiente tablero
 
    X | O | X
    ----------
      |   | X
    ----------
    O | O | X
    
 Como podemos ver, cada string representa una fila, y el puntito "." representa que el lugar esta vacio.
 
 Dada la lista inicial, nuestro programa debe imprimir si hay un ganador, o si la lista representa un tablero en el cual hay un 
 empate. En el ejemplo anterior, debemos imprimir "El jugador de las X's ha ganado!".
 
 Aqui tienes otras listas para testar tu programa, pero recuerda que debe ser capaz de decir quien gano en cualqueir situacion
 
 ["X.O", "XX.", "XOO"]
 
 ["OO.", "XOX", "XOX"]
 
 ["OOX", "XXO", "OXX"]
 
 -----------------------------------------------------
 
 Ejercicio 16
 
 Ana y Billie estan jugando un juego en equipo. Ana escoge un numero inicial entre 1 y 1000, que sea entero (no posee comas)
 y lo escribe en la pizarra.
 Billie entonces empieza a escribir una lista de numeros. Si el ultimo numero escrito es multiplo de 2, entonces 
 escribiran ese ultimo numero, dividido 2. Si por el contrario el ultimo numero escrito es impar, entonces escribiran
 ese ultimo numero, multiplicado por 3, y luego le sumaran uno a la respuesta. Ese resultado final sera el numero escrito en la pizarra
 En resumen:
 
 si n es par ---> escriben n/2
 si n es impar --> escriben 3*n+1
 
 El objetivo es parar cuando se haya escrito el numero "1" en la pizarra. Por ejemplo, si Ana escoge el numero 10, entoces la lista sera
 
 10, 5, 16, 8, 4, 2, 1 ( y la lista acaba)
 
 Ana y BIllie quieren encontrar la lista mas larga posible que pueden conseguir, dadas las condiciones del problema. Cual es el numero que deben escoger
 para conseguir su cometido?
 
 ----------------------------------------------------
 
 Ejercicio 17
 
 Haga que el usuario ingrese una cadena de string
 
 pass = input("Ingrese su contraseña: ")
 
 Imprima un mensaje al usuario informandole si su contraseña es lo suficientemente segura o no.
 La contraseña debe cumplir con los siguientes requisitos:
 1)Debe contener al menos 10 caracteres
 2)Debe contener al menos un numero
 3)Debe contener al menos una letra mayuscula y una minuscula
 
 Imprima el resultado del test. Es la contraseña segura o no?
 
 ---------------------------------------------------
 
 Ejercicio 18:
 
 En este ejercicio debemos trabajar con numeros binarios. Escriba la siguiente linea de codigo:
 
 num = int(input("Escriba un numero positivo"))
 
 El programa debe imprimir la cantidad de unos que tiene ese numero en representacion binaria.
 
 Si el usuario introduce el numero 17, entonces la representacion binaria es 10001, luego se debe imprimir el valor 2.
 
 ------------------------------------------------------
 
 Ejercicio 19:
 
 Ahora vamos a trabajar con codigo Morse. (Vea https://es.wikipedia.org/wiki/C%C3%B3digo_morse para saber mas). 
 Somos historiadores de la segunda guerra mundial, y vemos el siguiente mensaje codificado (copielo en la primera
 linea del script):

 poem = 'm.--- m.- m-- m.- m... ----- ----- m.--. .-. .. -. -.-. . ... .-   -.. .   --- .--- --- ...   -. . --. .-. --- ...   -.-. --- -.   ..- -.   ..-. ..- .-.. --. --- .-.   -.. .   .- -.-. . .-. --- ....- ----- --.- ..- .   . -.   -- ..   -.-. .. . .-.. ---   -.-. ..- ... - --- -.. .. .- ...   ..- -. .-   . ... - .-. . .-.. .-.. .-   -.. .   ..-. . ----- -- .   .- --. ..- .- .-. -.. .- .-. .- ...   - .-. . ...   -- . ... . ... ....-   ..- -.   .-.. ..- ... - .-. --- ....-   ..- -.   ... .. --. .-.. ---   . -. - . .-. --- ....- ----- m. - . .-. -. .- -- . -. - . .-----   m. -.   ...- .- -. --- ....-   --.- ..- .   -.-- .-   -. ---   ...- --- .-.. ...- . .-. . ..... ----- ----- m.-. . -.-. ..- . .-. -.. .- ...   .-.. .-   .--. .- .-. - .. -.. .-   -.. . .-..   .--. .- .-.. .. -.. ---   ...- .. .- .--- . .-. --- ----- -.-. --- -.   ... ..-   -- --- .-. .-. .- .-..   -.. .   .- -. .... . .-.. ---   --.- ..- .   .--. .- .-. .-   ... .. . -- .--. .-. .   ..-. ..- . ----- m-- --- .-. .. .-   . .-..   -... .-.. .- -. -.-. ---   -.-. .. .-. .. ---   -.. . .-..   ..- .-.. - .. -- ---   .-.. ..- -.-. . .-. --- ----- -.. .   .- --.- ..- . .-.. .-.. .-   .- --.. ..- .-..   - .- .-. -.. .   --.- ..- .   -. ..- -. -.-. .-   --- .-.. ...- .. -.. .- .-. . ----- ----- m. .-. .-   . .-..   ..- .-.. - .. -- ---   .. -. ... - .- -. - .   -.. .   -. ..- . ... - .-. --- ...   -.. ..- .-.. -.-. . ...   -.. .. .- ... ....- ----- -.. .   -. ..- . ... - .-. --- ...   -.-. .- .-. --- ...   ... ..- .--. .-.. .. -.-. .. --- ... ..... ..... .....   m.- .-.. -... .. -. .- ....-   -. ---   ... .- -... .. .- ... ----- --.- ..- .   ... .. -.   ...- --- .-.. ...- . .-.   .-   ...- . .-. -. --- ...   .--. --- .-.   ... .. . -- .--. .-. .   -.-. . .-. .-. .- .-. .- ... ----- ----- m.- --.- ..- . .-.. .-.. --- ...   --- .--- --- ...   -. . --. .-. --- ...   -.-. --- -.   ..- -.   ..-. ..- .-.. --. --- .-.   -.. .   .- -.-. . .-. --- ....- ----- --.- ..- .   .... .- ...   -.-. .-.. .- ...- .- -.. ---   . -.   . .-..   .- .-.. -- .-   -.. . .-..   .--. .- .-.. .. -.. ---   ...- .. .- .--- . .-. --- ....- ----- --.- ..- .   .--. .- .-. - .. ---   ..- -.   -.. .. .-   .--. .- .-. .-   ...- --- .-.. ...- . .-. ..... ..... .....   .--- .- -- .- ... ..... ----- ----- m-- .- -. ..- . .-..   m--- .-. - .. --..   m--. ..- . .-. .-. . .-. --- ..... '
 
 Nuestro objetivo sera descifrar el anterior mensaje. Para ello nos guiaremos del codigo morse (link arriba)
 Como podemos ver, es un string conformado por "-", "." y espacios. Para descifrarlo, solo tenemos que tener en cuenta
 cuatro cosas
 1) Palabras diferentes estan separadas por 3 (tres) espacios
 2) Caracteres diferentes estan separadas por un espacio
 3) Hemos agregado unos caracteres al codigo morse:
 a) ----- significara "\n"
 b) .---- significara "!"
 c) ..--- significara "?"
 d) ...-- significara "¿"
 e) ....- significara ","
 f) ..... significara "."
 4) Si la letra es mayuscula, el codigo de la letra empieza con una "m"
 
 Nuestros historiadores saben que el codigo anterior, cuando pasemos a string, sera un poema de un autor
 Paraguayo. Tu tarea es descifrar quien es el autor, cuyo nombre se encuentra dentro del poema.
 
 -------------------------------------------------------
 
 Ejercicio 20:
 
 Ahora somos vendedores de Sandias. Tenemos sandias de diferentes kilos, expresados en la siguiente lista
 
 pesos = [4, 3, 2, 5, 9, 2, 1]
 
 (Esta lista puede ser arbitariamente larga, define la tuya al comienzo del script, pero deben ser obligatoriamente 
 compuesta por enteros positivos). Entonces la lista ejemplo de arriba dice que tienes 8 sandias de pesos 4 kilos, 3 kilos, 2 kilos, etc etc
 Al mediodia vienen dos magnates de negocios queriendote comprar todas tus sandias. Estos magnates son muy competitivos entre ellos, 
 y no te compraran ninguna sandia si el otro magnate se lleva mas kilos de sandia que el. Tu como buen programador decides crear un 
 script que imprima si es posible vender todas tus sandias, de modo que los dos magnates esten felices.
 En el ejemplo de arriba, si le vendemos las sandias de 4 y 9 kilos al primer magnate, y las sandias de 3, 2, 5, 2 y 1 kilo al segundo
 entonces los dos magnates se llevaran 13 kilos de Sandia cada uno. Por lo tanto el programa debe imprimir "Con la lista inicial de sandias,
 es posible distribuir equitativamente los pesos". En caso de no poder hacerlo, el programa debe imprimir "Con la lista inicial de Sandias,
 es imposible distribuir equitativamente los pesos". 
 
 -----------------------------------------------------------

 Ejercicio 21:

 Debemos escapar de una peligros expedicion! Para este problema, somos
 Indiana Jones y debemos escapar de una piramide. Nosotros nos encontramos
 en el piso mas alto de la piramide, y debemos ir bajando de piso, hasta llegar
 al suelo. En cualquier cuarto del suelo hay una puerta de salida, asi que
 solo con llegar al suelo ya estamos a salvo. Sin embargo, en cada cuarto hay
 un  mercenario que nos pide oro.

 Vea el archivo pyramid.png que acompaña a los otros scripts en el material de apoyo. Es la piramide en la
 cual nos entontramos. Y cada numero representa la cantidad de oro que se debe pagar al pasar
 por ese cuarto. Ademas, dado que estamos en un cuarto, solo podemos pasar a uno de los dos siguientes
 cuartos: o el que esta un piso abajo y a la derecha, o el que esta un piso abajo y a la izquierda del
 cuarto donde nos encontramos. Es decir, siempre debemos bajar un piso. Queremos quedarnos con la mayor
 cantidad de oro posible en nuestra bolsa. Cual es el camino que hara esto posible?

 Devuelva un string que diga el camino a recorrer. I si debe ir a la izquierda y D si debe ir a la derecha
 Ejemplo: "IIDDIDIIIDDDIDII"

 ----------------------------------------------------------------

 Ejercicio 22:

 Escriba un programa que:

 1)Pida dos enteros positivos al usuario

 2)Imprima el maximo comun divisor, el minimo comun multiplo y la descomposicion
 prima de ambos numeros, en ese orden.

 -----------------------------------------------------------------

 Ejercicio 23:

 Ahora somos un hacker. Tenemos nuestro archienemigo: James Moriarty, a quien queremos robarle todo el dinero
 de su banco. James Moriarty tiene una contraseña hecha unicamente de digitos cuyo largor no conocemos.
 Lo que si sabemos es que el banco le pide a James exactamente tres de esos digitos de su contraseña cada vez
 que realiza la transaccion. Es decir, si la contraseña fuese 5592831, y el banco le pide el primer, segundo y
 quinto digito, entonces James digita el numero 558. Sabemos que el banco siempre le pide los digitos en orden
 es decir, si el banco le pide los digitos cuarto, y sexto, entonces ya no le puede pedir mas el quinto (tiene
 que ser orden ascendente). Hemos estado interceptando las ultimas 50 operacioes que James Moriarty hizo en su
 banco. Entonces sabemos los numeros que James estuvo mandando como confirmacion para el banco, pero no sabemos
 el orden que el banco le pidio para que mandase.
 Es nuestra mision descifrar la contraseña completa de James Moriarty, sabiendo que, entre todas las contraseñas
 posibles (dados esos 50 datos que tenemos) James tiene la mas corta posible. Para acceder a las ultimas 50
 transacciones de Moriarty, lea en su script el archivo keylog.txt, que contiene 50 lineas de numeros de tres
 cifras. (Vea en material de apoyo)

 -------------------------------------------------------------------

 Ejercicio 24:

 El año pasado, Arabia Saudita le concedio la primera ciudadania a un robot en este mundo.
 El robot, lastimosamente se ha aburrido, y es nuestro deber ayudarlo a pasar el tiempo.
 Ella nos dice que le gusta mucho el sudoku, pero que es incapaz de resolverlo con la logica
 humana. Para este ejercicio debemos elaborar un algoritmo que pueda resolver sudokus.
 Cada fila, columna y cuadrado de 3x3 debe tener exactamente un digito entre 1 y 9
 (las diagonales no cuentan). 
 Para este problema, deberemos leer el archivo sudoku.txt que se encuentra en el material de
apoyo. Contiene 50 sudokus separados por lineas, con el siguiente
 formato:

 003020600
 900305001
 001806400
 008102900
 700000008
 006708200
 002609500
 800203009
 005010300

 donde los ceros indican una casilla vacia. Debemos crear otro archivo de texto, soluciones.txt
 con el mismisimo formato que el archivo sudoku.txt, pero con las soluciones a todos los
 sudokus, para mostrarselas despues a nuestra amiga robot.

 Para testar, la solucion al sudoku de arriba es:

 483921657
 967345821
 251876493
 548132976
 729564138
 136798245
 372689514
 814253769
 695417382

 ---------------------------------------------------------------------------
 
 Ejercicio 25
 
 Es el año 2045, y somos parte de la tripulacion que la humanidad envió a Marte para colonizar otros planetas.
 Nuestro pasatiempo favorito aqui es jugar al PlayStation 42, la ultima consola que salio al mercado antes de
 haber dejado la tierra. Nuestro juego favorito es GTA San Andreas, que sabemos que tiene una secuencia de trucos
 que podemos presionar para desbloquear logros. Nuestro juego posee cuatro teclas, "A", "B", "X", "Y". Asi que
 los trucos solo pueden ser una secuencia de teclas de esos cuatro tipos. Existe una restriccion mas, que es 
 que la primera tecla no se puede repetir en la secuencia. Por ejemplo, "ABXXXY" y "BXYXAX" son trucos posibles
 pero "AXBXYYXA" no, pues la letra "A" se repite. 
 Nuestro objetivo es descubrir el truco que San Andreas tiene para nosotros. Para eso, nosotros podemos ir tecleando
 secuencias de letras de largor como maximo 4N al juego, donde N es el largor del truco (que nosotros sabemos, es un dato)
 Por ejemplo, si el truco es "ABXXXY", podemos teclear cualquier secuencia de largor como maximo 24. El juego nos 
 premiara con una cantidad de monedas, dependiendo de que tan parecida es la palabta que tecleamos con el verdadero truco
 El sistema de premiacion es el siguiente:
 -Te dara cero monedas si es que tu palabra no contiene la primera letra del truco original.
 -Luego, va a calcular la subpalabra mas larga que esta dentro de tu palabra y del truco y que contenga la primera letra 
 del truco. Por ejemplo si el truco es "ABXYY", y nosotros tecleamos:
 
 Palabra           |   Monedas recibidas
 "XXYYABYABXAY"    |     3
 "ABXYY"           |     5
 "ABXYYABXYY"      |     5
 ""                |     0
 "X"               |     0
 "BXYY"            |     0
 "YYXBA"           |     1
 "AY"              |     1
 
 Nosotros realmente no tenemos tiempo para ir tecleando todas las posibilidades, pero deberemos usar nuestras habilidades
 de programacion para hacer un script que adivine cual es el truco por nosotros. Entonces, el programa debera hacer lo
 siguiente:
 
 -Dejar que el usuario ingrese un numero N, entre 1 y 200, que representara el largor del truco.
 -Luego, debemos crear un truco de largor N, con la restriccion mencionada anteriormente.
 Este truco debe ser aleatorio, es decir, nosotros no debemos tener influencia alguna en como 
 se crea. (Investiga como hacer cosas aleatorias!)
 -Luego debemos hacer que nuestro script genere palabras para testear, y debemos agregar
 la cantidad de monedas que GTA nos da por esa palabra. A cada palabra que testeamos,
 se debe sumar un intento al registro.
 -Finalmente, deberemos imprimir con toda seguridad
 cual es el truco que GTA tiene escondido.
 
 Sin embargo, hay un problema. Como estamos en Marte, los ordenadores estan generalmente ocupados 
 recabando informacion, por lo que nuestro Python tiene limitaciones. Si tecleamos mas de 8000 intentos
 de adivinar el truco, nuestro ordenador priorizara Python por sobre otras tareas importantes para
 sobrevivir en Marte, y por lo tanto moriremos. Es nuestro deber adivinar el truco en menos de 8000 intentos.
 '''
