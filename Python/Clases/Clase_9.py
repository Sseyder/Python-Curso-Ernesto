'''
#* CLASE 9

#* SENTENCIAS CONDICIONALES ANIDADAS

Las sentencias condicionales anidadas, se presentan cuando tenemos una instruccion condicional dentro de otra instruccion condicional

'''

# Inicio del programa con una print en pantalla
print("\n=========")
print("Conversor")
print("========= \n")
# Print en pantalla del menu de opciones
print("Menu de opciones: \n")
print("Presiona 1 para convertir número a palabra.")
print("Presiona 2 para convertir palabra a número. \n")
# Capturamos mediante un input cual el la opcion a elegir
opcion = int(input("¿Cual es la opcion a elegir?: "))
# Condicionales respecto a la opcion elegida
# Conversion de números a letras
if opcion == 1:
    print("\nConversor de número a palabra: \n")
    # Logica de la conversion de numeros a palabras
    opcion1 = int(input("¿Que número deseas convertir a palabra?: "))
    if opcion1 == 1:
        print("\nEl número es 'UNO'.\n")
    elif opcion1 == 2:
        print("\nEl número es 'DOS'.\n")
    elif opcion1 == 3:
        print("\nEl número es 'TRES'.\n")
    elif opcion1 == 4:
        print("\nEl número es 'CUATRO'.\n")
    elif opcion1 == 5:
        print("\nEl número es 'CINCO'.\n")
    else:
        print("\nEse número no esta en la base de datos.\n")
# Conversion de palabra a número
elif opcion == 2:
    print("\nConversor de palabra a número: \n")
    # Logica dentro de la conversion de palabras a numeros
    opcion2 = (input("¿Que palabra deseas convertir a número?: "))
    opcion2 = opcion2.lower() # El metodo lower() es para modificar una string y que sea guardada nuevamente en la variable pero SOLO en minusculas
    if opcion2 == "uno":
        print("\nEl número es '1'.\n")
    elif opcion2 == "dos":
        print("\nEl número es '2'.\n")
    elif opcion2 == "tres":
        print("\nEl número es '3'.\n")
    elif opcion2 == "cuatro":
        print("\nEl número es '4'.\n")
    elif opcion2 == "cinco":
        print("\nEl número es '5'.\n")
    else:
        print("\nEsa palabra no esta en la base de datos.\n")
# Si no se cumple ninguna de las 2 opciones anteriores imprime en pantalla lo siguiente
else:
    print("\nEsta opcion no se encuentra disponible.\n")
# Print de fin del programa
print("Fin del programa.")