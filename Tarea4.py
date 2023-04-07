from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Configuración del controlador web de Chrome
driver = webdriver.Chrome()

# Navegar a la página de PlayStation Store de México
driver.get("https://store.playstation.com/es-mx/home/games")

# Esperar a que la página se cargue completamente
time.sleep(5)

# Iniciar sesión
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Inicia sesión')]"))
)
login_button.click()

email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "signin-email"))
)
email_input.send_keys("tu_correo_electronico")

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "signin-password"))
)
password_input.send_keys("tu_contraseña")

login_submit_button = driver.find_element_by_xpath("//button[contains(text(), 'Iniciar sesión')]")
login_submit_button.click()

# Esperar a que se cargue la página de inicio de sesión
time.sleep(5)

# Agregar un juego al carrito
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search-input-field"))
)

search_box.clear()
search_box.send_keys("Spider-Man Miles Morales PS5")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Agregar al carrito')]"))
)
add_to_cart_button.click()

# Esperar a que se cargue la página de carrito
time.sleep(5)

# Tomar una captura de pantalla del carrito
driver.save_screenshot("carrito.png")

# Eliminar un juego del carrito
remove_button = driver.find_element_by_xpath("//button[contains(text(), 'Eliminar')]")
remove_button.click()

# Esperar a que se actualice la página
time.sleep(5)

# Tomar una captura de pantalla del carrito actualizado
driver.save_screenshot("carrito_actualizado.png")

# Ver los juegos que están en oferta
ofertas_button = driver.find_element_by_xpath("//a[contains(text(), 'Ofertas')]")
ofertas_button.click()

# Esperar a que se cargue la página de ofertas
time.sleep(5)

# Tomar una captura de pantalla de la página de ofertas
driver.save_screenshot("ofertas.png")

# Cerrar sesión
profile_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Tu perfil']"))
)
profile_button.click()

logout_button = driver.find_element_by_xpath("//button[contains(text(), 'Cerrar sesión')]")
logout_button.click()

# Esperar a que se cierre la sesión
time.sleep(5)

# Tomar una captura de pantalla de la página de inicio
driver.save_screenshot("inicio.png")

# Cerrar el navegador
driver.quit()
