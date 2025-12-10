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
        
# Lectura del SCV
with open("bodega.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=",") # Preparamos el lector [cite: 165]
    
    for fila in lector:
        # 'fila' es una lista con los datos: ej. ['Leche', '1000', '50']
        print(f"Producto: {fila[0]} - Precio: {fila[1]}")