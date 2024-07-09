'''
#* CONCATENACION CON format()

Ya sabemos concatenar Strings con Strings y Strings con valores Int usando el operador "+"
Ademas sabemos que se puede separar elementos dentro de una funcion print() usando una coma.
Ahora vamos a utilizar format() para concatenar.

#? format():
El metodo format(), nos permite mostrar los valores contenidos en una variable
y utilizarlos dentro de una cadena de caracteres, sustituyendo el nombre de la variable con un juego de {},
ubicandolas en la posicion donde queremos que se muestren dichos valores.
Utilizando format() la concatenacion se puede realizar, sin importar que las variables sean de tipo String o de tipo númerico.

#? Sintaxis:
#* Opcion 1:
    "Hola {}, tenes {} años.".format(nombre, edad)
#* Opcion 2:
    "Hola {nombre}, tenes {edad} años.".format(nombre = 'Leonel', edad = 22)
#* Opcion 3:
    "Hola {0}, tenes {1} años.".format(nombre, edad)
'''

#* Ejemplo format():
# Opcion 1:
nombre = 'Leonel'
edad = 26
print('Hola {}, tenes {} años.'.format(nombre, edad))
# Opcion 2:
print('Hola {nombre_2}, tenes {edad_2} años.'.format(nombre_2 = 'Marcelo', edad_2 = 26))
# Opcion 3:
print('Hola {0}, tenes {1} años.'.format(nombre, edad))