''' Finalmente, debemos saber manejar datos externos. Por ejemplo, supongamos de
nuevo que somos meteorologos, y registramos ciertas temperaturas a traves del dia.
Entonces seria buena idea guardar los datos en un archivo externo.

Una tentativa puede ser crear la lista y usar el metodo .append 
'''
a = [14, 17, 22] #hacer append en el shell

'''
Pero eso por si solo no funciona. Cada vez que recibamos datos nuevos
deberemos entrar en el script e ingresarlos manualmente. 
Para solucionar eso, podemos abrir archivos externos y escribir en ellos.


with open('nombre_archivo', 'ar(+)w') as variable:
    texto = variable.read()
Entonces va a guardar un string con todo el texto en el. Un enter se
guarda como '\n'.
'''

with open('data.txt', 'r') as datos:
    texto = datos.read()
print(texto)

'''
Existen varias funciones que nos ayudaran
Ya vimos datos.read(), va a devolver un string con todos los caracteres restantes
datos.readline() va a devolver solo la primera linea
datos.tell() nos dira donde esta el cursor (no recibe argumentos)
datos.seek() nos pondra el cursor en el lugar indigado (para leer)

recuerden la diferencia entre los modos

r = Solo para leer.
r+ = Puede leer y sobreescribir, sin borrar lo que ya habia
a = va a escribir todo al final, sin borrar lo que habia. Si no hay archivo, lo crea
w = Va a sobreescribir todo lo que se agregue. Si no existe el archivo, se crea

'''

with open('data.txt', 'a') as archivo:
    string = 'Esto es lo que quiero agregar \n\n Python'
    archivo.write(string)
