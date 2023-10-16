#Busqueda Tabu 
import itertools #importamos la libreria para hacer permutaciones 

# Definir las ciudades y distancias
ciudades = ["Canada", "Toronto", "Vancouver"] #Crea una lista llamda cicudades con 3 elementos 
distacias = { #Diccionario que representa una lista entre la distancia de las ciudades 
    ("Canada", "Toronto"): 400,
    ("Canada", "Vancouver"): 2000,
    ("Toronto", "Vancouver"): 4000,
    ("Vancouver", "Canada"): 2000,
    ("Vancouver", "Toronto"): 4000,
    ("Toronto", "Canada"): 400
}

# Funcion para calcular la longitud de una ruta
def longitud_ruta(ruta):
    total_distacias = 0
    for i in range(1, len(ruta)):
        total_distacias += distacias[(ruta[i - 1], ruta[i])]
    return total_distacias

# Inicializaci�n
registro_ruta = None
distancia_mejor = float('inf')
tabu_list = []

# B�squeda Tab�
# Inicializa un bucle que se ejecutar� un m�ximo de 1000 veces, lo que representa el n�mero m�ximo de iteraciones permitidas en la b�squeda.
for _ in range(1000):
    # Genera todas las permutaciones posibles de las ciudades en el conjunto 'ciudades' tomadas de a 3.
    for perm in itertools.permutations(ciudades, 3):
        # Comprueba si la permutaci�n actual no est� en la lista tab�, lo que significa que esta ruta no se ha visitado recientemente.
        if perm not in tabu_list:
            # Calcula la longitud de la ruta actual utilizando la funci�n 'longitud_ruta'.
            current_length = longitud_ruta(perm)
            # Compara la longitud de la ruta actual con la mejor distancia encontrada hasta ahora.
            if current_length < distancia_mejor :
                # Si la longitud de la ruta actual es mejor que la mejor distancia registrada, actualiza la mejor distancia y la ruta correspondiente.
                registro_ruta = perm
                distancia_mejor  = current_length
                # Agrega la ruta actual a la lista tab� para evitar visitarla nuevamente en el futuro.
                tabu_list.append(perm)

# Mostrar el resultado
print("Mejor ruta encontrada:", registro_ruta)
print("Distancia total de viaje:", distancia_mejor)