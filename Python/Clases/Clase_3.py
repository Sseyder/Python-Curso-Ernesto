"""
#* CLASE 3

#* MANIPULACION DE STRINGS

Las strings son cadenas de caracteres que pueden estar compuestas de numeros, letras, simbolos y signos.

#* En Python existen distintos tipos de manipulaciones de Strings:
#? 1. Asignacion (Asignas una cadena de caracteres a otra. Utiliza el operador: +=)
#? 2. Concatenacion (Unir 2 cadenas o mas, para formar una cadena nueva de mayor tamaño. Utiliza el operador: +)
#? 3. Busqueda (Permite localizar, dentro de una string, una substring mas pequeña. Utiliza el operador: find)
#? 4. Extraccion (Sacar de una string, una porcion dentro de ella. Es necesario indicar la posicion a extraer: [1:8])
#? 5. Comparacion (Se utiliza para comparar dos strings y ver si son iguales. Utiliza el operador: ==)

"""

# Ejemplo Asignacion
mensaje = "Hola"
mensaje += " "
mensaje += "Leonel"
print(mensaje)

# Ejemplo Concatenacion
mensaje2 = "Hola"
espacio = " "
nombre = "Marcelo"
print(mensaje2 + espacio + nombre)

# Concatenacion con numeros
numero_1 = 5
numero_2 = 8
resultado = numero_1 + numero_2
#* COMO NO SE PUEDE CONCATENAR DOS TIPOS DISTINTOS DE VALORES (NUMEROS Y TEXTO) SE CAMBIA SU FORMATO Y SE GUARDA NUEVAMENTE
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

# Ejemplo Busqueda
mensaje3 = "Hola Leonel"
buscarSubstring = mensaje3.find("Leonel")
print(buscarSubstring)

# Ejemplo Extraccion
mensaje4 = "Hola Leonel"
extraerSubstring = mensaje4[1:8]
print(extraerSubstring)

# Ejemplo Comparacion
mensaje5 = "Leonel"
mensaje6 = "Leonel"
mensaje7 = "Hola"
print(mensaje5 == mensaje6)
print(mensaje7 == mensaje5)