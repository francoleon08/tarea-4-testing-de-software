# Proyecto de Pruebas con Pytest

Este proyecto utiliza Pytest para la ejecución de pruebas unitarias y la generación de reportes en formato HTML.

## Estructura del Proyecto

- `tests/`: Directorio que contiene todos los archivos de pruebas.
- `pytest.ini`: Archivo de configuración de Pytest.

## Configuración de Pytest

El archivo `pytest.ini` contiene la configuración para Pytest:

```ini
[pytest]
addopts = --html=report.html --self-contained-html
testpaths = tests
```

- `addopts`: Opciones adicionales para Pytest. En este caso, se genera un reporte HTML `report.html` que es auto-contenido.
- `testpaths`: Directorio donde se encuentran las pruebas.

## Cómo Ejecutar las Pruebas

Para ejecutar las pruebas y generar el reporte HTML, utiliza el siguiente comando:

```sh
pytest
```

El reporte se generará en un archivo llamado `report.html` en el directorio raíz del proyecto.

## Requisitos

- Python 3.x
- Pytest
- pytest-html (para la generación de reportes HTML)

## Configuración del Entorno virtual (opcional)

Se recomienda utilizar un entorno virtual para instalar las dependencias del proyecto.

```sh
python -m venv venv
```

Luego, activa el entorno virtual:

- Windows:

```sh
venv\Scripts\activate
```

- Linux/macOS:

```sh
source venv/bin/activate
```

## Instalación de Dependencias

Instala las dependencias necesarias utilizando `pip`:

```sh
pip install -r requirements.txt
```

## Comentarios

En el caso de no ejecutar las pruebas, el resultado lo puede ver en el archivo `report.html` que se encuentra en la raíz del proyecto.
Caso contrario, si ejecuta las pruebas, el resultado lo puede ver en la consola y en el archivo `report.html` el cual sobreescribirá el anterior.
