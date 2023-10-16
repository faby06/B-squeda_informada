#Busqueda en Anchura 

#importa la clase duque de la biblioteca
from collections import deque 

def buscar_ruta(ruta,inicio, fin):   #Aqui definimos una funcion con 3 argumentos ruta (el grafo representado como un diccionario de lista)
                                     #inicio(el nodo de inicio), fin(el nodo de destino al que se desea llegar)
    # Cola para almacenar los nodos a visitar
    cola = deque() #Aqui se crea una cola utilizando la clase deque
    cola.append([inicio]) # Se inicia la cola agregando una lista con el nodo de inicio 

    while cola :
        camino= cola.popleft() #Esto representa el camino actual que estamos explorando en este caso Mi_casa
        node = camino[-1] #El ultimo nodo en el camino actual se almacena en la variable 

        if node == fin: #Se verifica si el nodo actual (node) es igual al nodo de destino (fin) 
                        #Si son iguales, significa que se ha encontrado la ruta deseada desde el nodo de inicio hasta el nodo de destino
            return camino  # Ruta encontrada

        for neighbor in ruta.get(node, []):  #Este for lo que hace es recorrer toda la lista
            new_path = list(camino) # Se crea una copia del camino actual osea de la lista esto se hace para que no cambiemos directamente el camino actual si no sobre la capia trbajar 
            new_path.append(neighbor)#Se agrega el nodo vecino al nuevo camino creando así un nuevo camino que sigue la conexion con el nodo vecino
            cola.append(new_path)#Se agrega de nuevo a la cola para futuras exploraciones tener esa ruta contemplada

    return None  # No se encontró una ruta

#Grafo representado como un diccionario de listas 
ruta = {
    'Mi_Casa': ['Papeleria', 'Tienda'],
    'Papeleria': ['Mi_Casa', 'Cafeteria', 'Lavanderia'],
    'Tienda': ['Mi_Casa', 'OXXO'],
    'Cafeteria': ['Escuela'],
    'Lavanderia': ['Papeleria', 'OXXO'],
    'OXXO': ['Salon', 'Escuela']
}

inicio_nodo = 'Mi_Casa'
fin_nodo = 'Escuela'
result = buscar_ruta(ruta, inicio_nodo, fin_nodo)

if result:
     print("Ruta mas corta:",'->'.join(result))
else:
    print("No se encontro una ruta desde", inicio_nodo, "a",fin_nodo)
