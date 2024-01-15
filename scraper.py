import requests
from bs4 import BeautifulSoup
import json

def recolectarData():
        
    # URL inicial
    #url = "https://www.tcdb.com/ViewCard.cfm/sid/149667/cid/9623806?PageIndex=1"
    #url = "https://www.tcdb.com/ViewCard.cfm/sid/256822/cid/15841762/2002-Bandai-Naruto:-Coils-of-the-Snake-001-Inari?PageIndex=1"
    url = 'https://www.tcdb.com/ViewCard.cfm/sid/149666/cid/9623732?PageIndex=1'

    # Inicializar la lista
    url_list = []

    #first case
    url_list.append(url)

    #other cases
    # Iterar X veces
    for _ in range(28):
        # Realizar la solicitud HTTP
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parsear el contenido HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Encontrar el elemento <td>
            td_element = soup.find('td', {'align': 'right', 'valign': 'top', 'width': '20%'})

            # Verificar si se encontró el elemento
            if td_element:
                # Encontrar todas las etiquetas <a> dentro del elemento <td>
                a_elements = td_element.find_all('a')

                # Verificar si hay al menos un elemento <a>
                if a_elements:
                    # Obtener el enlace (href) del último <a>
                    link = a_elements[-1].get('href')

                    # Reemplazar el URL anterior con el nuevo enlace
                    url = "https://www.tcdb.com" + link
                    print("URL:", url)

                    # Agregar el nuevo URL a la lista
                    url_list.append(url)
                else:
                    print("No se encontraron etiquetas <a> dentro del elemento <td>.")
            else:
                print("No se encontró el elemento <td> con los atributos específicos.")
        else:
            print("Error al realizar la solicitud HTTP. Código de estado:", response.status_code)

    # Guardar la lista de URLs en un archivo JSON
    output_file_path = "./urls.json"
    with open(output_file_path, 'w') as output_file:
        json.dump(url_list, output_file, indent=2)

    print(f"Lista de URLs guardada en '{output_file_path}'.")


recolectarData()