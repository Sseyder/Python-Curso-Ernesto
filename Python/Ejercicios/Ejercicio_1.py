'''
#* EJERCICIO 1

Una empresa pide hacer un programa que cuente los dias de vacaciones a las que tiene derecho un empleado, tomando en cuenta las siguientes caracteristicas:

#* Existen 3 departamentos:
#? 1) Atención al cliente (Clave 123):
    #! Con 1 año, reciben 6 dias de vacaciones
    #! De 2 a 6 años, reciben 14 dias de vacaciones
    #! A partir de los 7 años, 20 dias de vacaciones
#? 2) Departamento de logistica (Clave 456):
    #! Con 1 año, reciben 7 dias de vacaciones
    #! De 2 a 6 años, reciben 15 dias de vacaciones
    #! A partir de los 7 años, 22 dias de vacaciones
#? 3) Genrencia (Clave 789):
    #! Con 1 año, reciben 10 dias de vacaciones
    #! De 2 a 6 años, reciben 20 dias de vacaciones
    #! A partir de los 7 años, 30 dias de vacaciones

#* REQUISITOS INDISPENSABLES:
El programa debe pedir "NOMBRE", "CLAVE DEL DEPARTAMENTO" y "ANTIGUEDAD"
Luego debe de mostrar un mensaje en pantalla que contenga el nombre del empleado y los dias de vacaciones a los que tiene derecho

'''
#TODO: PONER TODAS LAS TILDES
# Imprime en pantalla el nombre del programa
print("\n=======================================")
print("= VISUALIZADOR DE DIAS DE VACACIONES. =")
print("=======================================\n")
# Se crean las variables indispensables que necesita el programa
nombre = input("Por favor ingrese su nombre completo: ") #* NOMBRE DEL EMPLEADO
clave = int(input("\nPor favor ingrese su clave (En numeros): ")) #* CLAVE DEL DEPARTAMENTO EN EL QUE TRABAJA
años = float(input("\nIngrese los años de trabajo (En numeros): ")) #* AÑOS DE EMPLEAMIENTO
#* LOGICA DEL PROGRAMA
# Atencion al cliente
if clave == 123: #TODO: Mensaje en pantalla con departamento
    if años == 1 and años < 2 :
        print("\nFELICIDADES", nombre, " TENES 6 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    elif años >= 2 and años <= 6:
        print("\nFELICIDADES", nombre, " TENES 14 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    elif años >= 7:
        print("\nFELICIDADES", nombre, " TENES 20 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    else:
        print("\nUsted no goza de derecho a vacaciones.")
        print("\nFIN DEL PROGRAMA.")
# Departamento de logistica:
elif clave == 456: #TODO: Mensaje en pantalla con departamento 
    if años == 1 and años < 2 :
        print("\nFELICIDADES", nombre, " TENES 7 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    elif años >= 2 and años <= 6:
        print("\nFELICIDADES", nombre, " TENES 15 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    elif años >= 7:
        print("\nFELICIDADES", nombre, " TENES 22 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    else:
        print("\nUsted no goza de derecho a vacaciones.")
        print("\nFIN DEL PROGRAMA.")
# Gerencia:
elif clave == 789: #TODO: Mensaje en pantalla con departamento
    if años == 1 and años < 2 :
        print("\nFELICIDADES", nombre, " TENES 10 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    elif años >= 2 and años <= 6:
        print("\nFELICIDADES", nombre, " TENES 20 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    elif años >= 7:
        print("\nFELICIDADES", nombre, " TENES 30 DIAS DE VACACIONES.")
        print("\nFIN DEL PROGRAMA.")
    else:
        print("\nUsted no goza de derecho a vacaciones.")
        print("\nFIN DEL PROGRAMA.")
# Clave erronea ingresada:
else:
    print("\nLa clave ingresada no existe. Intentelo nuevamente.")
    print("\nFIN DEL PROGRAMA.")