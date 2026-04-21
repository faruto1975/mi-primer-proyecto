# Pre-Entrega Automation Testing

## Descripción

Proyecto de automatización web utilizando Selenium WebDriver y Pytest.
Se realizan pruebas automatizadas sobre la página SauceDemo.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Git
- GitHub

## Estructura del proyecto

tests/
    test_login.py

utils/
    driver_factory.py
    __init__.py

reports/
    reporte.html

## Casos de prueba incluidos

1. Login válido
2. Login inválido
3. Logout

## Instalación

Instalar dependencias:

pip install -r requirements.txt

## Ejecución

Ejecutar pruebas:

python -m pytest -v

Generar reporte HTML:

python -m pytest --html=reports/reporte.html