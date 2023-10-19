
# Importamos las bibliotecas necesarias.
import requests
from bs4 import BeautifulSoup

# Definimos una funci�n llamada buscar_en_google que toma una cadena de b�squeda como argumento.
def buscar_en_google(query):
    # Construimos la URL de Google para realizar la b�squeda.
    url = f"https://www.google.com/search?q={query}"

    # Realizamos una solicitud GET a la URL y almacenamos la respuesta en la variable response.
    response = requests.get(url)

    # Comprobamos si la solicitud fue exitosa (c�digo de estado 200).
    if response.status_code == 200:
        # Creamos un objeto BeautifulSoup para analizar el HTML de la p�gina.
        soup = BeautifulSoup(response.text, 'html.parser')

        # Usamos BeautifulSoup para encontrar todos los elementos <h3> con la clase "t".
        resultados = soup.find_all('h3', class_='t')

        # Iniciamos un bucle que recorre todos los resultados encontrados.
        for resultado in resultados:
            # Obtenemos el texto dentro del elemento <h3>, que es el t�tulo del resultado.
            titulo = resultado.get_text()

            # Buscamos el primer enlace <a> dentro del resultado y obtenemos el valor del atributo href.
            enlace = resultado.find('a')['href']

            # Imprimimos el t�tulo y el enlace del resultado en la consola.
            print(f"Resultado: {titulo}")
            print(f"Enlace: {enlace}\n")
    else:
        # Si la solicitud no tuvo �xito, mostramos un mensaje de error.
        print("No se pudo conectar a Google.")

# Verificamos si el script se est� ejecutando directamente (no importado como un m�dulo).
if __name__ == "__main__":
    # Solicitamos al usuario que ingrese una cadena de b�squeda.
    busqueda = input("Introduce tu busqueda: ")
    
    # Llamamos a la funci�n buscar_en_google con la cadena de b�squeda ingresada por el usuario como argumento.
    buscar_en_google(busqueda)