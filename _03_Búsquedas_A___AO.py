#Búsquedas A* y AO*

import heapq

grafo = {
    'Escuela': {'Parque': 10, 'Tienda': 7},
    'Parque': {'Casa': 5},
    'Tienda': {'Casa': 2, 'Parque': 5},
    'Casa': {},
    'Oxxo': {}
}

# Función de búsqueda A*
def buscar_ruta_A_estrella(grafo, inicio, objetivo):
    frontera = [(0, inicio)]  # Lista de prioridad de nodos a explorar (costo, nodo)
    visitados = set()  # Conjunto de nodos visitados

    while frontera:
        costo, nodo_actual = heapq.heappop(frontera)

        if nodo_actual == objetivo:
            return costo  # Devuelve el costo de la ruta

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        for vecino, costo_camino in grafo[nodo_actual].items():
            if vecino not in visitados:
                costo_total = costo + costo_camino
                heapq.heappush(frontera, (costo_total, vecino))

    return None  # No se encontró una ruta

inicio = 'Escuela'
objetivo = 'Oxxo'
costo_ruta = buscar_ruta_A_estrella(grafo, inicio, objetivo)

if costo_ruta is not None:
    print(f"La ruta mas corta desde {inicio} hasta {objetivo} tiene un costo de {costo_ruta}.")
else:
    print(f"No se encontro una ruta desde {inicio} hasta {objetivo}.")

