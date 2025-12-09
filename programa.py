import mis_funciones  # Sin el .py
# En el import, le estamos diciendo a Python que necesitamos el archivo 'mis_funciones' ya que debemos
# utilizar sus herramientas/funciones para evitar volver a programarlas porque ya están hechas

# Uso del módulo
texto = mis_funciones.saludar("Sobrino")
print(texto)

resultado = mis_funciones.suma_simple(5, 10)
print(resultado)