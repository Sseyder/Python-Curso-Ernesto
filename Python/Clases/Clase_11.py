'''
#* CLASE 11

#* OPERADORES DE ASIGNACION.

Un operador de asignacion se encarga de darle a la variable de la izquierda el valor de la derecha.
Los operadores de asignacion son:
#? = (Es el mas simple de todos, asigna una variable a un valor) Ej: x = 5
#? += (Suma a la variable del lado izquierdo con el valor del lado derecho) Ej: x = 3 -> x += 5 -> x = 8
#? -= (Resta a la variable del lado izquierdo con el valor del lado derecho) Ej: x = 8 -> x -= 5 -> x = 3
#? *= (Multiplica a la variable del lado izquierdo por el valor del lado derecho) Ej: x = 2 -> x *= 3 -> x = 6
#? /= (Divide a la variable del lado izquierdo por el valor del lado derecho junto con los valores despues de la coma) Ej: x = 10 -> x /= 3 -> x = 3.3
#? //= (Divide a la variable del lado izquierdo por el valor del lado derecho de forma entera, es decir sin los valores de la coma) Ej: x = 10 -> x //= 3 -> x = 3
#? **= (Calcula y asigna el exponente a la variable del lado izquierdo, con el valor del lado derecho) Ej: x = 2 -> x **= 5 -> x = 32
#? %= (Devuelve el resto de la division a la variable del lado izquierdo con el valor del lado derecho) Ej: x = 10 -> x %= 2 -> x = 0

'''

#* PROGRAMA DE INCREMENTO Y DECREMENTO DE VARIABLES.
# Creamos la variable nombre.
nombre = "Hola "
# Luego le sumamos otra cadena de caracteres que el usuario ingresa por teclado.
nombre += input("Escribe tu nombre: ")
# Imprime en pantalla la variable asignada entera con un texto adicaional.
print(nombre, ", esto es un programa de incremento y decremento de variables. \n")
# Incremento o aumento de numero.
print("Incremento o aumento: ")
# Asignamos valor inicial a la variable x e impriminos en pantalla cuanto vale.
x = 1
print("El valor inicial de la variable x es:", x)
# Sumamos 4 veces 1 a la variable x ya definida anteriormente e impriminos en pantalla el resultado final.
x += 1
x += 1
x += 1
x += 1
print("El valor final de la variable x es:", x, "\n")
# Decremento o disminucion.
print("Decremento o disminucion: ")
# Restamos 4 veces 1 a la variable x, con valor 5 e imprimimos en pantalla su valor.
print("El valor inicial de la variable x es:", x)
x -= 1
x -= 1
x -= 1
x -= 1
print("El valor final de la variable x es:", x, "\n")