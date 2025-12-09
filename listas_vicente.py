# definimos la lista con la que vamos a trabajar
lista = [1, 2, "hola", 3, "chao", 4, 5]
print(lista)

print(" ")
print(" ")

# Itero de una forma simple a través de la lista
# la variable 'elemento' al es la que recorre cada valor en la lista, entonces la puedo imprimir 
# y saber su valor en cada iteración
for elemento in lista:
    print(elemento)
    
print(" ")
print(" ")

# Aqui utilizo la funcion range dandole 2 argumentos, el 'desde' que es 1 y el 'hasta' que es 4.
# Dado que las listas tienen indices que posicionan cada elemento con un numero desde 0 al N, en este caso
# si le digo que quiero desde el elemento 1 (indice 0) hasta el 4 (indice 3), me va a imprimir los elementos de la posición 1 (que es el valor 2 en la lista)
# y tambien el elemento de la pisición 4-1 (por que 4-1? Porque la funcion de python range para el argumento 'hasta', no es inclusivo, 
# es decir si le dices que quieres el elemento 4, es como que le digas que quieres el elemento 3 (4-1))
for i in range(1, 4):
    print(lista[i])
    
print(" ")
print(" ")

# La funcion len (que significa longitud en inglés),
# permite saber la longitud de la lista (cuenta los elementos existentes en la lista, partiendo desde el 1)
print(f"La logitud es la lista es: {len(lista)}")

print(" ")
print(" ")

# Agregar elementos a la lsita
lista.append("good bye")
print(lista)

print(" ")
print(" ")

# Modificar un elemento de la lista
lista[0] = "uno"
print(lista)

print(" ")
print(" ")

# Eliminar elemento segun valor en la lista
lista.remove("chao")
print(lista)

print(" ")
print(" ") 

# Eliminar elemento segun valor en la lista
lista.remove("uno")
print(lista)

print(" ")
print(" ") 

# Eliminar elemento segun indice en la lista
lista.pop(3)
print(lista)

print(" ")
print(" ") 

# Eliminar el ultimo elemento (pop sin argumento por defecto borra el ultimo elemento de la lista)
lista.pop()
print(lista)

print(" ")
print(" ") 
  