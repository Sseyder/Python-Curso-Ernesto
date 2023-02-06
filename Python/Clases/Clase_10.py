'''
#* CLASE 10

#* OPARADORES RELACIONALES Y OPERADORES LOGICOS

=====================================================================================================
#* Operadores relacionales:
Los operadores relacionales son simbolos que se usan para comparar dos valores,
generalmente se utilizan en las sentencias condicionales para la toma de decisiones.

Al utilizar operadores relacionales dentro de una sentencia condicional,
si el resultado de la comparacion o condicion es correcto, esta sera considerada verdadera (true), 
en caso contrario sera considerada falsa (False).

#* LOS SIMBOLOS DE OPERACIONES RELACIONALES SON:
#? 1. < (Menor que) Ej: 5 < 7 ---> True
#? 2. > (Mayor que) Ej: 7 > 5 ---> True
#? 3. == (Igual que) Ej: 5 == 5 ---> True
#? 4. != (No igual a) Ej: 4 != 5 ---> True
#? 5. <= (Menor o igual) Ej: 5 <= 5 ---> True
#? 6. >= (Mayor o igual) Ej: 9 >= 5 ---> True
=====================================================================================================
#* Operadores logicos:
A veces es necesario utilizar mas de dos condiciones logicas dentro de una misma condicion,
con lo cual nos vemos en la necesidad de implementar multiples operadores relacionales para crear una expresion logica mucho mas compleja
Sin embargo, no es posible colocar 2 condiciones logicas dentro de una misma condicion, sin el apoyo de algun elemento que les indique a nuestros programas,
que se realizara la union de dos o mas condiciones logicas dentro de una misma condicion.

#* Para esto existen los OPERADORES LOGICOS, los cuales son:
#? 1. and (Conjunción)
#? 2. or (Disyunción)
#? 3. not (Negación)

#* Ej AND:
#? if num1 == 5 and num2 >= 5:
#?      print("Ambas condiciones se cumplieron")
#? else:
#?      print("Una de las condiciones no se cumplio")
    
#* Ej OR:
#? if num1 == 5 or num2 >= 5:
#?      print("Una o ambas condiciones se cumplieron")
#? else:
#?      print("Ninguna de las condiciones se cumplio")

#* Ej NOT:
#? if not num1 <= 5:
#?      print("La condicion se invirtio y se cumple al ser un numero menor o igual a 5")
#? else:
#?      print("No se cumple la condicion porque el numero es mayor o igual a 5")

'''

#* OPERADORES RELACIONALES
# Primero imprime en pantalla que va a realizar el programa
print("\nComparación de 2 números: \n")
# Inicializamos las variables de los 2 numeros a comparar con entrada de teclado
num1 = float(input("Introduzca el primer número a comparar: "))
num2 = float(input("Introduzca el segundo número a comparar: "))
# Muestra en pantalla los números a comparar
print("\nLos números a comparar son: ", round(num1, 2), " y ", round(num2, 2))
# Logica de operadores relacionales. Diferente que, mayor que y mayor e igual que.
if num1 == num2 :
    print("\nEl número 1 es 'IGUAL' al número 2 :D")
if num1 != num2:
    print("\nEl número 1 es 'DIFERENTE' al número 2 :D")
if num1 > num2 :
    print("\nEl número 1 es 'MAYOR' al número 2 :D")
if num1 >= num2 :
    print("\nEl número 1 es 'MAYOR O IGUAL' al número 2 :D")
if num1 < num2 :
    print("\nEl número 1 es 'MENOR' al número 2 :D")
if num1 <= num2 :
    print("\nEl número 1 es 'MENOR O IGUAL' al número 2 :D")


#* OPERADORES LOGICOS
#* Conjuncion
print("\nConjunción (and).\n")
# Creamos la variable num_uno
num1 = int(input("Escriba un número mayor a 2 y menor que 15: "))
# Creamos un if con la condicion logica and e imprime en pantalla el resultado
if num1 > 2 and num1 < 15:
    print("\nEl número", num1, "cumple con la condición.")
else:
    print("\nEl número", num1, "NO cumple con la condición.")

#* Disyunción
print("\nDisyunción (or).\n")
# Creamos la variable palabra
palabra = input("Para cumplir la condición, ingrese la palabra 'SI' o 'YES': ")
palabra = palabra.lower()
# if con la condicion logica e imprime en pantalla el resultado
if palabra == "si" or palabra == "yes" :
    print("\nLa condición se ha cumplido.")
else:
    print("\nLa condición 'NO' se ha cumplido.")

#* Negación
print("\nNegación (not).\n")
#Creamos la variable num1
num1 = int(input("Ingrese un numero igual a 5: "))
#if con la condicion logica e imprime en pantalla el resultado
if not num1 == 5:
    print("\nEl número es diferente de 5 y 'SI' cumple con la condición.")
else:
    print("\nEl número es igual a 5 y 'NO' cumple con la condición.")
