# 📦 Extractor y Descargador de Imágenes desde HTML

Este repositorio contiene dos scripts en Python que trabajan juntos para **extraer todas las URLs de imágenes contenidas en un archivo HTML** y posteriormente **descargar automáticamente esas imágenes** a una carpeta local.

Es útil cuando quieres clonar los recursos visuales de una página web, migrar un sitio, auditar imágenes, optimizar recursos o respaldar archivos multimedia.

---

## 🚀 ¿Qué hace este proyecto?

1. **Lee un archivo HTML local** (`index.html` por defecto).
2. **Escanea todas las etiquetas `<img>` y `<source>`**, incluyendo sus `src` y `srcset`.
3. **Extrae todas las URLs de imágenes**, detectando formatos comunes (png, jpg, webp, avif, etc.).
4. Guarda esas URLs en el archivo **`urls_imagenes.txt`**.
5. El segundo script toma ese archivo y **descarga todas las imágenes** en una carpeta llamada `imagenes_descargadas`.

Es un flujo ideal para agarrar imágenes de un sitio web que ya tienes descargado o exportado.

---

## 📁 Archivos del repositorio

### 1. **extractor_urls.py**

Este script:

* Lee el HTML.
* Extrae todas las URLs de imágenes usando **BeautifulSoup** y **regex**.
* Genera el archivo `urls_imagenes.txt`.

### 2. **descargar_imagenes.py**

Este script:

* Lee cada URL almacenada.
* Descarga cada imagen con `requests`.
* Guarda los archivos en `imagenes_descargadas/`.

---

## 📦 Requisitos

Instala las dependencias con:

```bash
pip install beautifulsoup4 requests
```

Dependencias principales:

| Librería                    | Uso                                                      |
| --------------------------- | -------------------------------------------------------- |
| **BeautifulSoup4**          | Parsear el HTML y extraer etiquetas `<img>` y `<source>` |
| **requests**                | Descargar las imágenes vía HTTP                          |
| **re** (incluida en Python) | Filtrar URLs por formatos de imagen                      |
| **os / urllib.parse**       | Manejo de rutas y procesamiento de URLs                  |

---

## 🧩 Cómo usarlo

### 1. Coloca tu archivo HTML

Pon el archivo en la raíz del repositorio.
Por defecto el código busca:

```
index.html
```

Puedes cambiarlo modificando esta constante:

```python
NOMBRE_ARCHIVO_HTML = 'index.html'
```

---

### 2. Ejecuta el extractor

```bash
python extractor_urls.py
```

Esto generará:

```
urls_imagenes.txt
```

---

### 3. Descargar las imágenes

```bash
python descargar_imagenes.py
```

El script creará la carpeta:

```
imagenes_descargadas/
```

Y guardará allí todos los archivos descargados.

---

## ⚠️ Notas importantes

* Si el HTML contiene rutas relativas, debes actualizar su origen o completar las rutas manualmente antes de usarlo.

* Funciona tanto con imágenes absolutas como relativas (siempre que el HTML las contenga tal cual).

* Si el servidor bloquea los requests por User-Agent, podrías añadir headers en `requests.get`.
