
# Importamos las bibliotecas necesarias.
import requests
from bs4 import BeautifulSoup

# Definimos una función llamada buscar_en_google que toma una cadena de búsqueda como argumento.
def buscar_en_google(query):
    # Construimos la URL de Google para realizar la búsqueda.
    url = f"https://www.google.com/search?q={query}"

    # Realizamos una solicitud GET a la URL y almacenamos la respuesta en la variable response.
    response = requests.get(url)

    # Comprobamos si la solicitud fue exitosa (código de estado 200).
    if response.status_code == 200:
        # Creamos un objeto BeautifulSoup para analizar el HTML de la página.
        soup = BeautifulSoup(response.text, 'html.parser')

        # Usamos BeautifulSoup para encontrar todos los elementos <h3> con la clase "t".
        resultados = soup.find_all('h3', class_='t')

        # Iniciamos un bucle que recorre todos los resultados encontrados.
        for resultado in resultados:
            # Obtenemos el texto dentro del elemento <h3>, que es el título del resultado.
            titulo = resultado.get_text()

            # Buscamos el primer enlace <a> dentro del resultado y obtenemos el valor del atributo href.
            enlace = resultado.find('a')['href']

            # Imprimimos el título y el enlace del resultado en la consola.
            print(f"Resultado: {titulo}")
            print(f"Enlace: {enlace}\n")
    else:
        # Si la solicitud no tuvo éxito, mostramos un mensaje de error.
        print("No se pudo conectar a Google.")

# Verificamos si el script se está ejecutando directamente (no importado como un módulo).
if __name__ == "__main__":
    # Solicitamos al usuario que ingrese una cadena de búsqueda.
    busqueda = input("Introduce tu busqueda: ")
    
    # Llamamos a la función buscar_en_google con la cadena de búsqueda ingresada por el usuario como argumento.
    buscar_en_google(busqueda)