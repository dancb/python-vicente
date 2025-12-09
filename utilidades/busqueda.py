lista = ["A", "B", "C", "A"]

# Forma segura de buscar, preguntamos si en 'lista' hay algun elemento con el valor 'B'
if "B" in lista:
    posicion = lista.index("B")
    print(f"Está en la posición: {posicion}") # Imprime 1
else:
    print("'B' no está en la lista")
    
# Contar elementos en la lista
print(len(lista)) # Dice el tamaño total de la lista (cuántos elementos tiene en total)
print(lista.count("C")) # Dice cuántas veces aparece un elemento específico