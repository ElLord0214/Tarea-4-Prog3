from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Configuración del controlador web de Chrome
driver = webdriver.Chrome()

# Navegar a la página de PlayStation Store
driver.get("https://store.playstation.com/")

# Esperar a que la página se cargue completamente
time.sleep(5)

# Lista de palabras clave para realizar búsquedas
keywords = ["videojuegos", "consolas", "ofertas", "demos", "accesorios"]

# Realizar 5 búsquedas aleatorias
for i in range(5):
    # Seleccionar una palabra clave aleatoria
    keyword = random.choice(keywords)

    # Esperar a que se cargue el cuadro de búsqueda
    search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "searchTerm"))
    )

    # Buscar la palabra clave en la página
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)

    
    # Esperar a que se cargue la página de resultados
    time.sleep(5)
    
    # Tomar una captura de pantalla y guardarla con el nombre de la palabra clave
    driver.save_screenshot(keyword + ".png")
    
    # Volver a la página principal
    driver.get("https://store.playstation.com/")
    time.sleep(5)

# Cerrar el navegador
driver.quit()
