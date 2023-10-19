import math
import random

# Función de energía: en este ejemplo, minimizamos f(x) = x^2
def energy(x):
    return x**2

# Parámetros del Temple Simulado
temperatura_inicial = 1000
temperatura_minima = 0.1
factor_enfriamiento = 0.9
iteraciones_por_temperatura = 100

# Inicialización
x = random.uniform(-10, 10)  # Solución inicial aleatoria
energia_actual = energy(x)
mejor_x = x
mejor_energia = energia_actual

# Bucle principal del Temple Simulado
temperatura = temperatura_inicial
while temperatura > temperatura_minima:
    for _ in range(iteraciones_por_temperatura):
        # Genera una solución vecina perturbando la solución actual
        vecino_x = x + random.uniform(-1, 1)
        energia_vecino = energy(vecino_x)
        
        # Calcula la diferencia de energía entre la solución actual y la vecina
        delta_energia = energia_vecino - energia_actual
        
        # Si la vecina es mejor o se acepta con una cierta probabilidad, cambia a la vecina
        if delta_energia < 0 or random.random() < math.exp(-delta_energia / temperatura):
            x = vecino_x
            energia_actual = energia_vecino
        
        # Actualiza la mejor solución encontrada
        if energia_actual < mejor_energia:
            mejor_x = x
            mejor_energia = energia_actual
    
    # Reduce la temperatura
    temperatura *= factor_enfriamiento

# Mostrar el resultado
print("Mejor solucion encontrada: x =", mejor_x)
print("Energia minima:", mejor_energia)
