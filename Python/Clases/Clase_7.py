"""
#* CLASE 7

#* ENTRADA DE DATOS DESDE EL TECLADO
Se realiza con el metodo:
#? - input()
"""

# Primer ejemplo de entrada de datos por teclado
palabra = input("Introduzca una palabra: ")
num_int = int(input("Introduzca un numero entero: "))
num_float = float(input("Introduzca un numero flotante: "))
num_complejo = complex(input("Introduzca un numero complejo: "))
print("String: ", palabra)
print("Numero entero: ", num_int)
print("Numero flotante: ", num_float)
print("Numero complejo: ", num_complejo)

# Segundo ejemplo de entrada de datos por teclado
nombre = input("¿Cual es tu nombre?: ")
print("Hola " + nombre + ", vamos a hacer una suma de numeros enteros :D")
num1 = int(input("Intruduzca el primer numero entero: "))
num2 = int(input("Intruduzca el segundo numero entero: "))
resultado = num1 + num2
print(nombre + " el resultado de la suma es:", resultado)