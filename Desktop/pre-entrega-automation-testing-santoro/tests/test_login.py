# tests/test_login.py

from utils.driver_factory import get_driver
from selenium.webdriver.common.by import By
import time


def test_login_valido():
    # Login con datos correctos

    driver = get_driver()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    assert "inventory" in driver.current_url

    driver.quit()


def test_login_invalido():
    # Login con datos incorrectos

    driver = get_driver()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("clave_invalida")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    error = driver.find_element(By.CLASS_NAME, "error-message-container")

    assert error.is_displayed()

    driver.quit()


def test_logout():
    # Cerrar sesión correctamente

    driver = get_driver()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    time.sleep(1)

    driver.find_element(By.ID, "logout_sidebar_link").click()

    time.sleep(2)

    assert "saucedemo" in driver.current_url

    driver.quit()