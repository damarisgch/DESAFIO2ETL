"""
Ejercicio 3: Conexión y Extracción de Datos desde una API
Utiliza la API pública "https://jsonplaceholder.typicode.com/posts" que proporciona datos de
publicaciones.
Escribe un programa en Python que haga una solicitud a la API, obtenga los datos en formato
JSON y los almacene en un DataFrame. Mostrar por pantalla los títulos de las primeras cinco
publicaciones.
"""
import requests
import pandas as pd

# URL de la API
url = "https://jsonplaceholder.typicode.com/posts"

# Hacer la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos JSON de la respuesta
    data = response.json()
    
    # Crear un DataFrame a partir de los datos JSON
    df = pd.DataFrame(data)
    
    # Mostrar los títulos de las primeras cinco publicaciones
    first_five_titles = df['title'].head(5)
    
    print("Títulos de las primeras cinco publicaciones:")
    for title in first_five_titles:
        print(title)
else:
    print(f"Error en la solicitud: Código {response.status_code}")
