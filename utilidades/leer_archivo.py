# Leer todo el archivo de una.
# "r" significa READ (Leer)
# la funcion 'with' se encarga de abrir el archivo y tambien cerrarlo cuando termina el bloque de ejecucion.
# Tienes que tener claro lo anterior, 'with' lo mencionan bastante en tu ppt de utilidades
with open("mi_archivo.txt", "r") as archivo:
    contenido_completo = archivo.read()
    print(contenido_completo)

# Si intentas usar 'archivo' aquí fuera, dará error porque ya se cerró automáticamente

print(" ")
print(" ")

# Leer el archivo linea por linea
with open("mi_archivo.txt", "r") as archivo:
    lista_de_lineas = archivo.readlines()
    # Ahora es una lista normal, podemos iterar:
    for linea in lista_de_lineas:
        print(f"Leído: {linea}") # .strip() quita el salto de línea sobrante
