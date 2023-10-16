#Búsqueda en Profundidad Iterativa

#Aqui se hace una busqueda minima 
def Busqueda_iterativa(grafo, nodo_inicial, nodo_objetivo):
    profundidad_maxima = 0 
    while True: #Comienza con una profucndidad maxima igual a 0 y este bucle va seguir iterando hasta recorrer todo el grafo 
        visitados = set()
        resultado =  Busqueda_limitada(grafo, nodo_inicial, nodo_objetivo, profundidad_maxima, visitados)
        if resultado is not None: #si no se encuentra solucion se incrementa 1 para la proxima iteracion 
            return resultado
        profundidad_maxima += 1
#Aqui se realiza una busqueda maxima 
def Busqueda_limitada(grafo, nodo, objetivo, profundidad_maxima, visitados):
    # Verifica si hemos alcanzado la profundidad máxima y si el nodo actual es el objetivo
    if profundidad_maxima == 0 and nodo == objetivo:
        return [nodo]
    # Si no hemos alcanzado la profundidad máxima.
    elif profundidad_maxima > 0:
        # Marca el nodo actual como visitado.
        visitados.add(nodo)
        # Itera a traves de los vecinos del nodo actual.
        for vecino in grafo[nodo]:
            # Si el vecino no ha sido visitado en esta iteración.
            if vecino not in visitados:
                # Realiza una búsqueda limitada desde el vecino.
                camino = Busqueda_limitada(grafo, vecino, objetivo, profundidad_maxima - 1, visitados)
                # Si se encontró un camino (camino no es None), retorna el camino actualizado.
                if camino is not None:
                    return [nodo] + camino
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

nodo_inicial = 'A'
nodo_objetivo = 'D'

resultado = Busqueda_iterativa(grafo, nodo_inicial, nodo_objetivo)
if resultado:
    print("Camino encontrado:", " , ".join(resultado))
else:
    print("No se encontro un camino.")
