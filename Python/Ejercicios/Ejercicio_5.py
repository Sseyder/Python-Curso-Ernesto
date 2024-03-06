'''
#* EJERCICIO 5:
Desarrollar un programa que imprima en pantalla la sucesion de Fibonacci desde el numero 0
hasta el numero 1597, de manera horizontal

Sucesion de Fibonacci:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

#? Requerimientos Indispensables:
#? El programa debe tener como maximo de 7 lineas de codigo
'''
num1, num2 = 0, 1
while num2 <= 1597:
    print(num1, num2, end=" ")
    num1 = num1 + num2
    num2 = num1 + num2