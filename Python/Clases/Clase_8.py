'''
#* CLASE 8

#* IF ELSE ELIF

Una sentencia condicional, es una instruccion o grupo de instrucciones que se ejecutan cuando se establece una condicion logica.
Al cumplir esa condicion se ejecuta el programa.
Las sentencias condicionales nos ayudan a controlar la toma de decisiones dentro de un programa.
Comprueban que una condicion sea verdadera o falsa y en base a eso llevan a cabo una accion.

#* En Pyhton se utilizan de la siguiente manera:
#? if -condicion logica- : 
#?      instruccion
#? elif -condicion logica- :
#?      instruccion
#? else:
#?      instruccion
'''


#* Ejemplo if else basico, un promedio entre 3 examenes parciales
# Arranca con una impresion en pantalla sobre que es el programa
print("===============================================================")
print("Sistema para calcular el promedio de un alumno con 3 parciales.")
print("=============================================================== \n")
# A continuacion pide el nombre del alumno mediante un input
nombre = input("¿Cual es tu nombre?: \n")
# Luego le pide ingresar las notas de las 3 materias, contando los decimales
parcial1 = float(input(nombre + ", ¿Cual es tu calificación en el primer parcial?: "))
parcial2 = float(input(nombre + ", ¿Cual es tu calificación en el segundo parcial?: "))
parcial3 = float(input(nombre + ", ¿Cual es tu calificación en el tercer parcial?: \n"))
# Calcula el promedio de los 3 parciales
promedio = (parcial1 + parcial2 + parcial3) // 3
# Sentencia if que imprime en pantalla un mensaje si el cuatrimestre tiene una calificacion superior a 6, contando los decimales
if promedio >= 6:
    print("Felicidades, " + nombre + ' "APROBASTE" el cuatrimestre con: ', round(promedio, 2))
else:
    print("Que lastima, " + nombre + ', no estudiaste nada :c. "REPROBASTE" el cuatrimestre con: ', round(promedio, 2))
# Print de finalizacion del programa
print("Fin del programa.")


#* Ejemplo elif basico, convertidor de numeros a letras
# Arranca con una impresion en pantalla sobre que es el programa
print("\n=======================================")
print("¡¡¡¡Convertidor de números a letras!!!!")
print("======================================= \n")
# En un principio pide ingresar por teclado un numero
num = int(input("¿Que número deseas convertir?: \n"))
# Si el numero ingresado es uno de los que estan dentro de la sentencia if se realiza la impresion en pantalla
if num == 1:
    print("El número es 'UNO' \n")
elif num == 2:
    print("El número es 'DOS' \n")
elif num == 3:
    print("El número es 'TRES' \n")
elif num == 4:
    print("El número es 'CUATRO' \n")
elif num == 5:
    print("El número es 'CINCO' \n")
elif num == 69:
    print("El número es 'EL NÚMERO DEL SEXO ;D' \n")
else:
    print("El programa solo compara hasta el numero 5, sin contar al 69 que es un caso excepcional \n")
# Agregamos un print para la finalizacion del programa
print("Fin del programa.")