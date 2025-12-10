import csv # Necesario importarlo para trabajar con archivos csv

# Leemos todo el archivo mi_archivo.txt de una sola vez.
# "r" significa READ (leer)
# 'with' abre y cierra el archivo automáticamente al terminar el bloque.
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
        print(f"Leído: {linea}")
        
# Lectura del SCV
with open("bodega.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=",") # Preparamos el lector [cite: 165]
    
    for fila in lector:
        # 'fila' es una lista con los datos: ej. ['Leche', '1000', '50']
        print(f"Producto: {fila[0]} - Precio: {fila[1]}")
