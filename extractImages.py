import requests
from bs4 import BeautifulSoup
import json
import os
from scraper import recolectarData 

recolectarData()

def extraer_imagen(url):
    # Realizar la solicitud a la página web
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el contenido HTML de la página
        html_content = response.text

        # Analizar el HTML con Beautiful Soup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Seleccionar todos los elementos <img>
        img_tags = soup.find_all('img', class_='img-fluid')

        # Verificar si hay al menos un elemento <img>
        if len(img_tags) > 0:
            # Seleccionar el primer elemento <img> en la lista
            img_tag = img_tags[2]

            # Obtener la URL absoluta de la imagen
            src_relative = img_tag.get('src')
            src_absolute = f"https://www.tcdb.com{src_relative}"

            return src_absolute
        else:
            print(f"No se encontraron elementos <img> en la página {url}")
    else:
        print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")

def descargar_imagen(url, folder):
    # Realizar la solicitud para obtener la imagen
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el nombre del archivo desde la URL
        filename = os.path.join(folder, os.path.basename(url))

        # Guardar la imagen en la carpeta especificada
        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"Imagen descargada y guardada en {filename}")
    else:
        print(f"No se pudo descargar la imagen desde {url}")

# Cargar las URLs desde el archivo JSON
with open('urls.json', 'r') as file:
    urls = json.load(file)

# Lista para almacenar los URLs de las imágenes
links_imagenes = []

# Crear la carpeta "cartas" si no existe
folder = 'cartas'
if not os.path.exists(folder):
    os.makedirs(folder)

# Iterar sobre las URLs y extraer las imágenes
for url in urls:
    imagen_url = extraer_imagen(url)
    if imagen_url:
        print(f"URL de imagen para {url}: {imagen_url}")
        links_imagenes.append(imagen_url)
        descargar_imagen(imagen_url, folder)
    else:
        print(f"No se pudo extraer la imagen para {url}")

# Guardar los URLs de las imágenes en un archivo JSON
with open('linksImagenes.json', 'w') as file:
    json.dump(links_imagenes, file)

print(f"Se ha guardado el archivo 'linksImagenes.json' en la carpeta raíz y se han descargado las imágenes en la carpeta '{folder}'.")
