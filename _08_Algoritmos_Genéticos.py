#Algoritmos Genéticos
import random

# Función de aptitud: Maximizar f(x) = x^2
def fitness(x):
    return x**2

# Configuración del AG
tama_poblacion = 100
probabilidad_mutacion = 0.1
num_generaciones = 100

# Inicialización de la población
poblacion = [random.uniform(-5, 5) for _ in range(tama_poblacion)]

# Bucle principal del AG
for generacion in range(num_generaciones):
    nueva_poblacion = []

    for _ in range(tama_poblacion):
        # Selección de dos padres aleatorios
        padre1 = random.choice(poblacion)
        padre2 = random.choice(poblacion)

        # Recombinación (cruce)
        hijo = (padre1 + padre2) / 2

        # Mutación
        if random.random() < probabilidad_mutacion:
            hijo += random.uniform(-0.1, 0.1)

        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion

# Encontrar la mejor solución
mejor_solucion = min(poblacion, key=fitness)
mejor_valor = fitness(mejor_solucion)

print("Mejor solucion encontrada: x =", mejor_solucion)
print("Valor maximo encontrado:", mejor_valor)



