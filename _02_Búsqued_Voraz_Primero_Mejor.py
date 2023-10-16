#Búsqueda Voraz Primero el Mejor

from queue import PriorityQueue

# Creamos un grafo
mapa = {
    'Casa': [('Parque', 5), ('Tienda', 2)], #Los numeros respresentan los minutos 
    'Parque': [('Escuela', 10)],
    'Tienda': [('Escuela', 5)],
    'Escuela': []
}

# Función para la búsqueda voraz primero el mejor
def voraz_primero_el_mejor(mapa, inicio, destino): #Crea una funcion con 3 parametros 
    frontera = PriorityQueue()
    frontera.put((0, inicio))  # Inicio desde la Casa con costo 0
    visitados = set()

    while not frontera.empty():
        costo, ubicacion_actual = frontera.get()

        if ubicacion_actual == destino:
            print("Has llegado a la Escuela desde tu Casa:", costo, "minutos")
            break

        if ubicacion_actual not in visitados:
            visitados.add(ubicacion_actual)

            for vecino, tiempo_viaje in mapa[ubicacion_actual]:
                if vecino not in visitados:
                    frontera.put((tiempo_viaje, vecino))

inicio = 'Casa'
destino = 'Escuela'
voraz_primero_el_mejor(mapa, inicio, destino)
