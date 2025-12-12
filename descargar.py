import requests
import os
from urllib.parse import urlparse

# --- Configuración ---
NOMBRE_ARCHIVO_ENTRADA = 'urls_imagenes.txt'
CARPETA_DESCARGA = 'imagenes_descargadas'
# ---------------------

def descargar_imagenes_de_lista(nombre_archivo_lista, carpeta_destino):
    """
    Lee una lista de URLs desde un archivo y descarga cada imagen
    en la carpeta de destino.
    """
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        print(f"Carpeta de destino '{carpeta_destino}' creada.")

    try:
        with open(nombre_archivo_lista, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de URLs '{nombre_archivo_lista}'.")
        return

    total_urls = len(urls)
    descargadas_exito = 0

    print(f"\nIniciando la descarga de {total_urls} imágenes...")

    for i, url in enumerate(urls):
        print(f"[{i + 1}/{total_urls}] Descargando: {url}...", end="")

        try:
            # 1. Obtener el nombre del archivo de la URL
            path = urlparse(url).path
            # Esto toma la última parte de la URL, que suele ser el nombre del archivo (ej: camiones-iconos1-260x178.png)
            nombre_archivo = os.path.basename(path)

            # 2. Descargar el contenido de la imagen
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status() # Lanza un error para códigos de estado HTTP 4xx/5xx

            # 3. Guardar la imagen
            ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
            with open(ruta_completa, 'wb') as f:
                # Escribe el contenido binario (b) de la imagen
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            descargadas_exito += 1
            print(" ✅ OK.")

        except requests.exceptions.RequestException as e:
            print(f" ❌ FALLÓ (Error de conexión/HTTP: {e})")
        except Exception as e:
            print(f" ❌ FALLÓ (Error inesperado: {e})")


# --- EJECUCIÓN ---
descargar_imagenes_de_lista(NOMBRE_ARCHIVO_ENTRADA, CARPETA_DESCARGA)
print(f"Imágenes guardadas en la carpeta: './{CARPETA_DESCARGA}'")