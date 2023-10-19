#Búsqueda de Haz Local
import random

# Función de optimización: f(x) = x^2
def f(x):
    return x**2

# Parámetros
x = random.uniform(-10, 10)  # Solución inicial aleatoria
paso = 0.1  # Tamaño del paso para buscar vecinos
num_iteraciones = 100  # Número máximo de iteraciones

# Búsqueda de Haz Local
for _ in range(num_iteraciones):
    actual = f(x)  # Evaluar la calidad de la solución actual

    # Generar dos soluciones vecinas (izquierda y derecha)
    izquierda = x - paso
    derecha = x + paso

    # Evaluar la calidad de las soluciones vecinas
    calidad_izquierda = f(izquierda)
    calidad_derecha = f(derecha)

    # Elegir el mejor vecino
    if calidad_izquierda < calidad_derecha and calidad_izquierda < actual:
        x = izquierda
    elif calidad_derecha < calidad_izquierda and calidad_derecha < actual:
        x = derecha

# Resultado
mejor_x = x
mejor_valor = f(x)

print("Mejor solucion encontrada: x =", mejor_x)
print("Valor minimo encontrado:", mejor_valor)