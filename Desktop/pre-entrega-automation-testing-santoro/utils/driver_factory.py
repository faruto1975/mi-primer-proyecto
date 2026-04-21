# utils/driver_factory.py

"""
Configuración del navegador Chrome.
Archivo auxiliar reutilizable para Selenium.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """
    Crea y devuelve una instancia del navegador Chrome.
    """

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    return driver