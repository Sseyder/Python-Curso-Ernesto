'''
#* PROGRAMA DE BUSQUEDA, AGREGADO, CAMBIO Y BORRADO DE LISTAS
#* (Por ahora SOLO Libros y Mangas. Series y peliculas se agregaran en futuras actualizaciones)

'''

import json
import os

#* Definimos las listas vacias para los mangas y los libros
mangas = []
libros = []

#* Función para agregar nuevos elementos a las listas
def agregar_elemento(lista, nombre_lista):
    respuesta = input(f"¿Desea agregar nuevos elementos a la lista {nombre_lista}? (si/no): ")
    if respuesta.lower() == "si":
        while True:
            nuevo_elemento = input(f"Ingrese un nuevo elemento para la lista {nombre_lista} o presione enter para omitir: \n")
            if nuevo_elemento != "":
                lista.append(nuevo_elemento)
            else:
                break
    else:
        print("No se han agregado nuevos elementos a la lista.\n")

#* Función para buscar elementos en las listas
def buscar_elemento(lista, nombre_lista):
    buscar = input(f"¿Desea buscar un elemento en la lista {nombre_lista}? (si/no): ")
    if buscar.lower() == "si":
        termino_busqueda = input("Ingrese un término de busqueda o presione enter para omitir: \n")
        if termino_busqueda != "":
            resultados_busqueda = []
            for elemento in lista:
                if termino_busqueda.lower() in elemento.lower():
                    resultados_busqueda.append(elemento)
            if resultados_busqueda:
                print(f"Resultados de la búsqueda en la lista {nombre_lista}:\n")
                for resultado in resultados_busqueda:
                    print("- " + resultado)
            else:
                print(f"No se encontraron resultados de la búsqueda en la lista {nombre_lista}.\n")
        else:
            print("No se ingresó ningún término de búsqueda.\n")
    else:
        print(f"No se buscará en la lista {nombre_lista}.\n")

#* Función para guardar las listas en un archivo JSON
def guardar_listas():
    with open("listas.json", "w") as archivo:
        datos = {"mangas": mangas, "libros": libros}
        json.dump(datos, archivo)

#* Función para cargar las listas desde un archivo JSON
def cargar_listas():
    if os.path.exists("listas.json"):
        with open("listas.json") as archivo:
            datos = json.load(archivo)
            mangas.extend(datos["mangas"])
            libros.extend(datos["libros"])

#* Función para modificar un elemento en una lista
def modificar_elemento(lista, nombre_lista):
    modificar = input(f"¿Desea modificar un elemento en la lista {nombre_lista}? (si/no): ")
    if modificar.lower() == "si":
        termino_busqueda = input("Ingrese el elemento a modificar o presione enter para omitir: \n")
        if termino_busqueda != "":
            indice = -1
            for i, elemento in enumerate(lista):
                if termino_busqueda.lower() in elemento.lower():
                    indice = i
                    break
            if indice >= 0:
                nuevo_elemento = input("Ingrese el nuevo valor del elemento o presione enter para omitir: \n")
                if nuevo_elemento != "":
                    lista[indice] = nuevo_elemento
                    print(f"Elemento modificado en la lista {nombre_lista}.\n")
            else:
                print(f"No se encontró el elemento en la lista {nombre_lista}.\n")
    else:
        print(f"No se han modificado elementos en la lista {nombre_lista}.\n")

#* Función para borrar elementos de las listas
def borrar_elemento(lista, nombre_lista):
    elemento_a_borrar = ""
    while elemento_a_borrar not in ["si", "no"]:
        elemento_a_borrar = input(f"¿Desea borrar algún elemento de la lista {nombre_lista}? (si/no): ").lower()
        if not elemento_a_borrar:
            elemento_a_borrar = "no"
    if elemento_a_borrar == "si":
        elemento_a_borrar = input(f"Ingrese el elemento que desea borrar de la lista {nombre_lista}: \n").lower()
        if elemento_a_borrar in lista:
            lista.remove(elemento_a_borrar)
            print(f"Se ha eliminado {elemento_a_borrar} de la lista {nombre_lista}.\n")
        else:
            print(f"{elemento_a_borrar} no se encuentra en la lista {nombre_lista}.\n")
    else:
        print("No se han eliminado elementos.\n")

#* Función para imprimir las listas
def imprimir_listas(mangas, libros):
    mostrar_listas = ""
    while mostrar_listas.lower() not in ["si", "no"]:
        mostrar_listas = input("¿Desea mostrar las listas de MANGAS y LIBROS? (si/no): ")
        if mostrar_listas == "":
            mostrar_listas = "no"
    if mostrar_listas.lower() == "si":
        print("\nMangas:")
        for manga in mangas:
            print("- " + manga)
        print("\nLibros:")
        for libro in libros:
            print("- " + libro)
    else:
        print("\n¡Hasta luego!")

#* Cargar las listas desde el archivo JSON
cargar_listas()

#* Agregar elementos a las listas
agregar_elemento(mangas, "MANGAS")
agregar_elemento(libros, "LIBROS")

#* Modificar elementos en las listas
modificar_elemento(mangas, "MANGAS")
modificar_elemento(libros, "LIBROS")

#* Ordenar las listas alfabeticamente
mangas.sort()
libros.sort()

#* Buscar elementos en las listas
buscar_elemento(mangas, "MANGAS")
buscar_elemento(libros, "LIBROS")

#* Borrar elementos de las listas
borrar_elemento(mangas, "MANGAS")
borrar_elemento(mangas, "LIBROS")

#* Guardar las listas en el archivo JSON
guardar_listas()

#* Preguntar si se quieren imprimir las listas
imprimir_listas(mangas, libros)