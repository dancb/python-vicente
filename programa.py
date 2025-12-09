import mis_funciones  # Sin el .py
# En el import, le estamos diciendo a Python que necesitamos el archivo 'mis_funciones' ya que debemos
# utilizar sus herramientas/funciones para evitar volver a programarlas porque ya están hechas

# Uso del módulo
texto = mis_funciones.saludar("Sobrino")
print(texto)

print(" ")
print(" ") 

resultado = mis_funciones.suma_simple(5, 10)
print(resultado)

print(" ")
print(" ") 

# Codigo pequeño para crear una tabla y explicarla (la explciación en la tabla se encuentra en (imagenes/tabla_secuencia_programa.png)
val = 0
for i in range(3): # Aqui el range al no tener 'desde' y un 'hasta', crea una lista de numeros temporal de 3 elementos (indice; 0, 1 y 2)
    num = i * 2
    val = val + num
print(val)
