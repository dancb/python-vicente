import random
# Como en cualquier lenguaje de programación, estos traen funcionaldiades ya conocidas y resueltas
# de tal manera que los programadores no tengan que reinventar la rueda porque ya está hecha.
# Entonces Python por ejemplo tiene un modulo con funciones de tipo 'random' y una vez que las importas ya puedes utilizarlas.

# Ejemplo que simula un dado
dado = random.randint(1, 6)
print(f"El valor del dado es: {dado}")

# Ejemplo de elegit un ganador de forma random
nombres = ["Ana", "Vicente", "Carla"]
ganador = random.choice(nombres)
print(f"Ganó: {ganador}")