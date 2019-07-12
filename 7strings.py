'''Ahora vamos a aprender a manipular strings. Lo primero que debemos saber es 
que un string puede ser visto como una lista de caracteres, en el sentido que tienen
indexado
'''

b = 'Esto es una oracion'
print(b[2])

#for x in b:
#    print(x)

'''
Tambien tienen otros metodos parecidos a las listas. Como hay muchos, lo mejor
que se puede hacer es ver la documentacion. Mostraremos los mas utiles

string.count(char) \\ va a contar la cantidad de veces que char aparece en string
string.index(char) \\ Devuelve la posicion de char en string. Retorna error si
char no se encuentra en string.
string.upper() \\ conierte el string en mayusculas
string.lower() \\ convierte el string en minusculas
string.replace(viejo, nuevo) \\ reemplaza los viejos strings por los nuevos
string.split(char) \\ crea una lista donde el separador es el string char
'''


string = 'Veamos como nos va con este string.'

#string.count('n')
#string.index(' ')
#string.upper()
#string.lower()
#string.replace("e", "E")
#string.split(" ")