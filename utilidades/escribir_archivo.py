import csv # Necesario importarlo para trabajar con archivos csv

# CODIGO PARA TRABAJAR CON ARCHIVOS DE TEXTO
lista_compras = ["Manzanas", "Peras", "Uvas"]

with open("compras.txt", "w") as archivo: # "w" para escribir [cite: 138]
    # Forma 1: Escribir texto manual
    archivo.write("Lista de Supermercado:\n") # \n es obligatorio para bajar de línea [cite: 140]
    
    # Forma 2: Escribir una lista (OJO: No pone espacios ni enters)
    archivo.writelines(lista_compras) 
    # Esto escribirá: "ManzanasPerasUvas" (Todo pegado)s

    # Forma 3: Lo correcto para listas (Recorrer y escribir)
    archivo.write("\n\n--- Corregido ---\n")
    for fruta in lista_compras:
        archivo.write(fruta + "\n") # Agregamos el salto manualmente
    

# CODIGO PARA TRABAJAR CON ARCHIVOS CSV
datos = [
    ["Producto", "Precio", "Stock"], # Encabezados
    ["Leche", 1000, 50],
    ["Pan", 500, 100]
]

# Escritura/creación del archivo CSV
with open("bodega.csv", "w", newline='') as csvfile: # newline='' evita líneas vacías extra en Windows
    escritor = csv.writer(csvfile, delimiter=",") # Preparamos el escritor [cite: 159]
    
    # Escribimos fila por fila
    for fila in datos:
        escritor.writerow(fila) # writerow escribe una lista como una línea del CSV [cite: 160]
      

# Creamos el archivo mi_archivo.txt si no existe para que sea leido en el archivo leer_archivo.py.
# "w" significa WRITE (escribir). Si el archivo no existe, lo crea.
with open("mi_archivo.txt", "w") as archivo:
    archivo.write("Este es el contenido inicial del archivo.\nLínea 2 del archivo.")