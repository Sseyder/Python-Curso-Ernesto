'''
#* EJERCICIO 3:

Desarrollar un programa que solicite 3 numeros enteros desde teclado al usuario.
Luego el programa debera determinar e indicar cual de los 3 numeros es el mas grande.

#* REQUISITOS INDISPENSABLES:
#? El programa debe mostrar cual de los 3 numeros es el mas grande junto con la frase "El número X es el mas grande de los 3".
'''

#* Titulo del programa.
print("\n========================================================================================")
print("= Progama para determinar cual es el número mas grande entre 3 números enteros distintos =")
print("==========================================================================================\n")
#* Escribimos las variables a elegir mediante ingreso de teclado.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
#* Logica del programa.
if num1 > num2 and num1 > num3:
    print("El número", num1, "es el mas grande de los tres.\n")
    print("Fin del programa.")
else:
    if num2 > num3 :
        print("El número", num2, "es el mas grande de los tres.\n")
        print("Fin del programa.")
    else:
        print("El número", num3, "es el mas grande de los tres.\n")
        print("Fin del programa.")