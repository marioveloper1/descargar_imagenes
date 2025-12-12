import re
from bs4 import BeautifulSoup
import os

# --- Configuración ---
NOMBRE_ARCHIVO_HTML = 'index.html' # <-- ¡CAMBIA ESTO POR EL NOMBRE DE TU ARCHIVO O MODIFICA EL NOMBRE DE TU ARCHIVO POR ESTE!
NOMBRE_ARCHIVO_SALIDA = 'urls_imagenes.txt'
# ---------------------

def extraer_urls_imagenes_de_archivo(nombre_archivo):
    """Lee HTML y extrae URLs de imágenes."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            html_doc = file.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        return []

    soup = BeautifulSoup(html_doc, 'html.parser')

    # Patrón para formatos de imagen comunes
    image_pattern = re.compile(r'\.(png|jpg|jpeg|gif|svg|webp|avif)$', re.IGNORECASE)

    urls_encontradas = set()

    # Buscar etiquetas <img>
    for img_tag in soup.find_all('img'):
        src = img_tag.get('src')
        if src and image_pattern.search(src):
            urls_encontradas.add(src)

        # Buscar en srcset
        srcset = img_tag.get('srcset')
        if srcset:
            for part in srcset.split(','):
                url = part.strip().split(' ')[0]
                if url and image_pattern.search(url):
                    urls_encontradas.add(url)

    # Buscar etiquetas <source>
    for source_tag in soup.find_all('source'):
        src = source_tag.get('srcset')
        if src:
            for part in src.split(','):
                url = part.strip().split(' ')[0]
                if url and image_pattern.search(url):
                    urls_encontradas.add(url)

    return sorted(list(urls_encontradas))

def guardar_urls_en_archivo(urls, nombre_archivo_salida):
    """Guarda cada URL en una nueva línea del archivo de salida."""
    if not urls:
        print("No hay URLs para guardar.")
        return

    try:
        with open(nombre_archivo_salida, 'w', encoding='utf-8') as f:
            for url in urls:
                f.write(url + '\n')
        print(f"\n✅ Extracción completada. {len(urls)} URLs guardadas en '{nombre_archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")


# --- EJECUCIÓN ---
lista_de_urls = extraer_urls_imagenes_de_archivo(NOMBRE_ARCHIVO_HTML)
guardar_urls_en_archivo(lista_de_urls, NOMBRE_ARCHIVO_SALIDA)