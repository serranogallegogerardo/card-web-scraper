import requests
from bs4 import BeautifulSoup
import json
import time
import random


################


#Modifica el valor de firstUrl para utilizar
firstUrl = "https://www.tcdb.com/ViewCard.cfm/sid/149666/cid/9623732?PageIndex=1"


################

base_url = "https://www.tcdb.com"
url_list = []

#primer y segundo link se toman como un caso aislado
def firstCase(url):
    
    url_list.append(url)
    print(url)

    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar el elemento <td>
        td_element = soup.find('td', {'align': 'right', 'valign': 'top', 'width': '20%'})
        if td_element:
            a_elements = td_element.find_all('a')


            link = a_elements[-1].get('href')
        
            # Reemplazar el URL anterior con el nuevo enlace
            url = base_url + link
            
            # Agregar el nuevo URL a la lista
            url_list.append(url)
            print(url)

            return url

def recolectarData():
    
    # URL inicial
    url = firstUrl
    #"https://www.tcdb.com/ViewCard.cfm/sid/149667/cid/9623807?PageIndex=1"
    url = firstCase(url)
    # Iterar hasta que no haya más botones "Next"
    while url:

        #relentizar para no sobrecargar tanto al servidor
        time.sleep(random.uniform(1, 4))
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
                
                # Verificar si hay al menos dos elementos <a>
                if len(a_elements) > 1:
                    # Obtener el enlace (href) del último <a>
                    link = a_elements[-1].get('href')

                    # Reemplazar el URL anterior con el nuevo enlace
                    url = base_url + link
                    print(url)

                    # Agregar el nuevo URL a la lista
                    url_list.append(url)
                else:
                    print("Fin. Menos de 2 etiquetas <a> dentro del elemento <td>.")
                    break  # Salir del bucle si no hay más botones "Next"
            else:
                print("No se encontró el elemento <td> con los atributos específicos.")
                break  # Salir del bucle si no hay más botones "Next"
        else:
            print("Error al realizar la solicitud HTTP. Código de estado:", response.status_code)
            break  # Salir del bucle si hay un error en la solicitud HTTP

        # Verificar si solo hay un botón "Prev" y no hay botón "Next"
        prev_button = soup.find('a', {'href': True, 'class': 'btn-primary', 'type': 'button', 'title': 'Previous Card'})
        next_button = soup.find('a', {'href': True, 'class': 'btn-primary', 'type': 'button', 'title': 'Next Card'})

        if not next_button and prev_button:
            print("Solo queda un botón 'Prev', finalizando la iteración.")
            break

    # Guardar la lista de URLs en un archivo JSON
    output_file_path = "./urls.json"
    with open(output_file_path, 'w') as output_file:
        json.dump(url_list, output_file, indent=2)

    print(f"Lista de URLs guardada en '{output_file_path}'.")

recolectarData()
