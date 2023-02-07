'''
#* EJERCICIO 2

Desarrollar un programa que solicite un numero entero desde teclado al usuario,
posteriormente debera determinar si el numero introducido es par o impar.

#* REQUERIMIENTOS INDISPENSABLES:
#? El mensaje debera mostrar en pantalla el numero introducido por el usuario y la frase "Este numero es par/impar".
#? Por ejemplo:
#! "El numero 8 es par"
#! "El numero 5 es impar"

'''

#* Titulo del programa
print("\n======================================================")
print("= Programa que determina si un número es par o impar =")
print("======================================================\n")
#* Creamos la variable numero, siendo esta un numero entero
numero = int(input("Por favor, introduzca un número entero: "))
#* Si el numero ingresado es divisible por 2 y su resto da 0, muestra en pantalla en mensaje
if numero % 2 == 0 :
    print("\nEl número,", numero, " es par\n")
    print("Fin del programa")
#* Caso contrario muestra este otro mensaje
else:
    print("\nEl número,", numero, " es impar")
    print("Fin del programa")