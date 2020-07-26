'''
La ultima estructura que necesitaremos es el bucle while. Este es como un bucle if
de largor indefinido:

while booleano:
    ---------------------
    |                   |
    |                   |
    |    Aqui van las   |
    |   instrucciones   |
    |                   |
    |                   |
    ---------------------
(esto va fuera del bloque)

El bucle while entrara en el paquete de instrucciones solamente si el booleano
de la primera linea tiene el valor verdadero. Ademas, cada vez que finaliza el 
bloque, volvera a analizar el booleano, y volvera a entrar en caso de que sea
aun verdadero.

Tengan precaucion, el bucle while debe ser usado solamente cuando sabemos que 
se saldra de ahi. Si la condicion boolean es siempre verdadera, python estara
en el commando de instrucciones de por vida, y el programa no terminara
'''
while False:
    print("Ayuda!, no puedo salir")

#para detener un programa que se esta tardando demasiado, apriete ctrl + c

#A continuacion, un ejemplo comun de uso de while

x = float(input("Ingrese un numero positivo: "))

while x < 0:
    print("Usted ha ingresado un numero negativo!")
    x = int(input("Ingrese un numero POSITIVO: "))
    if x==-42:
        break
    
#Vemos que el loop se reproduce siempre que la condicion sea verdadera.
