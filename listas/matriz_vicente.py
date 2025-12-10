# Aqui una matriz que está compuesta por listas (lista de listas)
matriz = [
    [1, 2, 3],
    ["hola", "hello", "ciao"],
    [True, False, True]
]

print("MATRIX ")
print(matriz[1])
print("MATRIX ")

# El primer 'for' elige la fila completa
# El segundo 'for' corresponde a la columna 
# y el cruce de la fila con la columna te da la 'celda' (si lo imaginamos como una hoja de excel)
for fila in matriz:
    for columna in fila:
        print(f"El valor en la celda actual es: {columna}")
        print(f"El valor del eje x es: {fila}")
        print(" ")
        
print(" ")
print(" ")

# Aqui lo mismo que arriba pero de una forma un poco mas sofisticada, usando funciones range y len de python
for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        print(f"El valor en la celda actual es: {matriz[x][y]}")
        print(f"El valor del eje x es: {matriz[x]}")
        print(" ")


