'''
#* EJERCICIO 4:
#* Desarrollar una calculadora.
Desarrollar una calculadora de operaciones aritmeticas basicas, esta debe tener un menu de opciones mediante input de usuario

#? Requerimientos que la calculadora debe tener:
#? 1. La calculadora debe tener las siguientes caracteristicas. Suma, Resta, Multiplicacion, division, division entera, exponente y resto.
#? 2. La calculadora debe tener un menu de opciones donde el usuario pueda elegir cual es la opcion que desea ejecutar.
#? 3. La caluladora solo debe utilizar una variable
'''
print("= Calculadora Simple con una sola variable =")
print("\n====================")
print("= Menu de Opciones =")
print("====================\n")

print("1. Suma.")
print("2. Resta.")
print("3. Multiplicacion.")
print("4. Division.")
print("5. Division Entera.")
print("6. Exponente.")
print("7. Resto.\n")

num = int(input("Ingrese la opcion deseada: "))

if num == 1:
    print("Elegiste la opcion SUMA\n")
    num = int(input("Ingrese el primer numero: "))
    num += int(input("Ingrese el segundo numero: "))
    print(f"El resultado de la SUMA es: {num}")
elif num == 2:
    print("Elegiste la opcion RESTA\n")
    num = int(input("Ingrese el primer numero: "))
    num -= int(input("Ingrese el segundo numero: "))
    print(f"El resultado de la SUMA es: {num}")
elif num == 3:
    print("Elegiste la opcion MULTIPLICACION\n")
    num = int(input("Ingrese el primer numero: "))
    num *= int(input("Ingrese el segundo numero: "))
    print(f"El resultado de la MULTIPLICACION es: {num}")
elif num == 4:
    print("Elegiste la opcion DIVISION\n")
    num = int(input("Ingrese el primer numero: "))
    num /= int(input("Ingrese el segundo numero: "))
    print(f"El resultado de la DIVISION es: {num}")
elif num == 5:
    print("Elegiste la opcion DIVISION ENTERA\n")
    num = int(input("Ingrese el primer numero: "))
    num //= int(input("Ingrese el segundo numero: "))
    print(f"El resultado de la DIVISION ENTERA es: {num}")
elif num == 6:
    print("Elegiste la opcion EXPONENTE\n")
    num = int(input("Ingrese el primer numero: "))
    num **= int(input("Ingrese el segundo numero: "))
    print(f"El resultado del EXPONENTE es: {num}")
elif num == 7:
    print("Elegiste la opcion RESTO\n")
    num = int(input("Ingrese el primer numero: "))
    num %= int(input("Ingrese el segundo numero: "))
    print(f"El resultado del RESTO es: {num}")
else:
    print("\nLA OPCION ELEGIDA NO ES VALIDA.")