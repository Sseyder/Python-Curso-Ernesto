"""
#* CLASE 6

#* TIPOS DE DATOS

Un tipo de dato es un atributo de los datos que indica a una computadora y al programador
sobre que clase de datos se va a manejar

#* En Python existen los siguientes tipos de datos:
#? 1. Enteros (Numeros que no tienen decimales, tanto positivos como negativos. Son expresados con int o long)
#? 2. Flotantes (Son los que tienen decimales, tanto positivos como negativos. Son expresados con float)
#? 3. Numeros Complejos (Son aquellos que tienen una parte real y una imaginaria. Son expresados con el tipo complex)
#? 4. Cadenas (Mas llamadas Strings, son cadenas de caracteres. Se expresan con comillas simples, dobles o triples.)
#? 5. Booleanos (Solo puede tener 2 valores True o False. Se expresan con bool)

"""

# Ejemplo de numero entero
num = 15
print (num, type(num))

# Ejemplo de numero flotante
num_float = 15.98156
print(num_float, type(num_float))

# Ejemplo numero complejo
num_complejo = 5 + 6j
print(num_complejo, type(num_complejo))

# Ejemplo string
cadena = "Hola mundo!"
print(cadena, type(cadena))

# Ejemplo booleano
booleano = 3 == 3
print(booleano, type(booleano))