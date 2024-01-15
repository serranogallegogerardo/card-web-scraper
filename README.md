Carta Scraper Bot
=================

Descripción
-----------

Este es un bot scraper de cartas diseñado para extraer imágenes de cartas de un sitio web específico (www.tcdb.com). 
El bot está escrito en Python y utiliza un entorno virtual para gestionar sus dependencias.

Requisitos previos
------------------

*   Python 3.x instalado en tu sistema.
*   Virtualenv para crear un entorno virtual.

Configuración inicial
---------------------

1.  Crea un entorno virtual en la raíz del proyecto utilizando el siguiente comando:
    
    `virtualenv env`
    
2.  Activa el entorno virtual:
    
    *   En Windows:
        
        `.\env\Scripts\activate`
        
    *   En Linux/Mac:
      
        `source env/bin/activate`
        
3.  Instala las dependencias necesarias ejecutando:
    
    bash
    
    `pip install -r requirements.txt`
    
Configuración del scraper
-------------------------

Abre el archivo `scraper.py` y busca la variable `firstUrl` en la parte superior del archivo.
Reemplaza la URL actual con el enlace del sitio web que contiene las cartas que deseas extraer.

`# scraper.py  # Cambia la siguiente URL por la del sitio que contiene las cartas url = "https://www.ejemplo.com/cartasDeAgua-Index=1"`

Ejecutar el scraper
-------------------

Una vez que hayas configurado la URL, puedes ejecutar el scraper utilizando el siguiente comando:

`python scraper.py`

Este comando iniciará el proceso de extracción de urls de imágenes de las cartas en el sitio web proporcionado.

Una vez que tengas el urls.json, puedes extraer imagenes utilizando el siguiente comando:

`python extractImages.py`


Notas adicionales
-----------------

*   Asegúrate de tener una conexión a Internet estable durante la ejecución del scraper, ya que depende de la descarga de imágenes desde el sitio web.
    
*   Si surge algún problema durante la ejecución, verifica que las dependencias estén instaladas correctamente y que la URL proporcionada sea válida.
    
*   Este bot scraper se proporciona como un ejemplo básico y puede requerir ajustes según las especificaciones del sitio web que estés tratando de extraer.

Imágenes del Proyecto
--------------------

![image](https://github.com/serranogallegogerardo/card-web-scraper/assets/98660245/4668a0d7-ca76-499c-9e8a-debbd4f10782)


¡Listo! Ahora deberías tener un entorno virtual configurado y el scraper listo para extraer imágenes de cartas según tu configuración. ¡Buena suerte!
