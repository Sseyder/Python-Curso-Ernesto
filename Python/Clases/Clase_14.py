'''
#* BREAK y CONTINUE

En Python los Bucles pueden ser interrumpidos, o simplemente, dejar de ejecutarse
para iniciar una nueva iteracion (Repeticion).

Para lograr eso se utilizan las sentencias:
#? - break y continue

#? BREAK
Se utiliza para detener la ejecucion de la iteracion y salir de ella,
el programa podra continuar con la ejecucion del codigo que se encuentre
fuera del bucle

#? CONTINUE
Permite detener la iteracion actual y volver al principio del bucle
para realizar una nueva iteracion si es que la condicion se sigue cumpliendo
'''

#* Ejemplo break
print("While con sentencia Break \n")
contador = 0
while contador <= 10:
    contador += 1
    if contador == 5:
        break
    print("Valor actual de contador: ", contador)
print("Fin del programa. La sentancia Break se ha ejecutado")

#* Ejemplo continue
print("\nWhile con sentencia Continue \n")
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print("Valor actual de contador: ", contador)