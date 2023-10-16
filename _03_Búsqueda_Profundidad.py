#Búsqueda en Profundidad

def busqueda_en_profundidad(grafo, nodo_inicial, visitados):
    if nodo_inicial not in visitados: # Si lo que esta en el nodo inicial no esta en visitados va imprimir lo que este en el nodo inicial 
        #
        print(nodo_inicial)  # Imprimir o realizar alguna accion con el nodo visitado
        visitados.add(nodo_inicial)  # Marcar el nodo como visitado utilizando el .add
        for vecino in grafo[nodo_inicial]: #Aqui se obtiene en el grafo los nodos vecinos de la lista original 
            if vecino not in visitados: #Se verifica si en los vecinos que no se hayan visitados eso nodos en visitados 
                busqueda_en_profundidad(grafo, vecino, visitados) #Si esto se cumple del nodo no se a visitado se llama a la funcion para visitarlo 

#Creamos un grato con diferentes nodos 
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

nodo_inicial = 'A' #Aqui mencionamos de donde queremos partir en Este caso desde la A
visitados = set()  # Conjunto para llevar un registro de los nodos visitados

print("Recorrido en profundidad del grafo:") # Se manda imprimir cada nodo visitado en este caso de la A a la E 
busqueda_en_profundidad(grafo, nodo_inicial, visitados)
