import heapq

# Grafo que representa las conexiones entre ubicaciones y sus distancias
ruta_desde_hasta = {
    "Casa": {"Calle A": 2, "Calle B": 3}, #Los numero representan la distancia
    "Calle A": {"LaTienda": 5},
    "Calle B": {"LaTienda": 4},
    "LaTienda": {},
}

def encontrar_ruta(grafo, ubicacion_inicio, ubicacion_destino):
    abierto = [(0, ubicacion_inicio)] #Es una lista de nodos para explorar en donde se tiene el costo actual y el nombre de la ubicacion
    antecesores = {} #Es un diccionario que rastrea el nodo anterior para cada ubicacion
    costo_g = {ubicacion: float('inf') for ubicacion in grafo} #Se utiliza para analizar la ruta 
    costo_g[ubicacion_inicio] = 0

    while abierto: #Realiza la busqueda y actualiza los datos para encontrar la ruta mas corta
        costo_actual, ubicacion_actual = heapq.heappop(abierto)

        if ubicacion_actual == ubicacion_destino: #Si ambas ubicaciones son iguales se recontruye la ruta actual 
            ruta = reconstruir_ruta(antecesores, ubicacion_actual)
            return ruta
        
        #Aqui se itera en la lista para encontrar la ruta mas corta 
        for vecino, distancia in grafo[ubicacion_actual].items():
            costo_tentativo_g = costo_g[ubicacion_actual] + distancia
            if costo_tentativo_g < costo_g[vecino]:
                antecesores[vecino] = ubicacion_actual
                costo_g[vecino] = costo_tentativo_g
                costo_f = costo_tentativo_g + heuristica(vecino, ubicacion_destino)
                heapq.heappush(abierto, (costo_f, vecino))

    return None

def heuristica(ubicacion, destino):
    # Heurística simple: distancia en línea recta entre ubicaciones
    return 0
#Aqui se va recorriendo los caminas hasta llegar a una ruta optima 
def reconstruir_ruta(antecesores, ubicacion_actual):
    ruta = [ubicacion_actual]
    while ubicacion_actual in antecesores:
        ubicacion_actual = antecesores[ubicacion_actual]
        ruta.insert(0, ubicacion_actual)
    return ruta

#Aqui le digo de donde quiero que emepieze y hasta donde quiero que termine 
ubicacion_inicio = "Casa"
ubicacion_destino = "LaTienda"

ruta_optima = encontrar_ruta(ruta_desde_hasta, ubicacion_inicio, ubicacion_destino)
print("Ruta mas corta:", ruta_optima)