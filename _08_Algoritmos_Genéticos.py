#Algoritmos Gen�ticos
import random

# Funci�n de aptitud: Maximizar f(x) = x^2
def fitness(x):
    return x**2

# Configuraci�n del AG
tama_poblacion = 100
probabilidad_mutacion = 0.1
num_generaciones = 100

# Inicializaci�n de la poblaci�n
poblacion = [random.uniform(-5, 5) for _ in range(tama_poblacion)]

# Bucle principal del AG
for generacion in range(num_generaciones):
    nueva_poblacion = []

    for _ in range(tama_poblacion):
        # Selecci�n de dos padres aleatorios
        padre1 = random.choice(poblacion)
        padre2 = random.choice(poblacion)

        # Recombinaci�n (cruce)
        hijo = (padre1 + padre2) / 2

        # Mutaci�n
        if random.random() < probabilidad_mutacion:
            hijo += random.uniform(-0.1, 0.1)

        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion

# Encontrar la mejor soluci�n
mejor_solucion = min(poblacion, key=fitness)
mejor_valor = fitness(mejor_solucion)

print("Mejor solucion encontrada: x =", mejor_solucion)
print("Valor maximo encontrado:", mejor_valor)



