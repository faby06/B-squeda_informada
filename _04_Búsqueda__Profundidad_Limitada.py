#Búsqueda en Profundidad Limitada

def busqueda_en_profundidad_limitada(grafo, nodo_actual, visitados, profundidad_maxima):
    if profundidad_maxima == 0: #Si el valor que le de abajo a esta varible es 0 no me va buscar nada porque me esta regresando el mismo valor 
        return

    if nodo_actual not in visitados: # Se verifica si el nodo actual no se a visitado 
        print(nodo_actual)  # Imprimir o realizar alguna acción con el nodo visitado
        visitados.add(nodo_actual)

        for vecino in grafo[nodo_actual]: #Este for esta iterando y guarda los datos en la varible vecinos
            busqueda_en_profundidad_limitada(grafo, vecino, visitados, profundidad_maxima - 1) 
            #Se manda llamar la funcion en la cual vuelve a recorrer pero produndidad maxima la van reduciendo en 1 cada que avanzamos por los nodos 

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

nodo_inicial = 'C'
visitados = set()  # Conjunto para llevar un registro de los nodos visitados
profundidad_maxima = 4 # Profundidad máxima deseada

print(f"Recorrido en profundidad limitada (profundidad maxima: {profundidad_maxima}) del grafo:")
busqueda_en_profundidad_limitada(grafo, nodo_inicial, visitados, profundidad_maxima)
