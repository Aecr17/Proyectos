
# Librerias importadas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Interactuar con la pagina web
driver=webdriver.Chrome()
driver.get("https://demoqa.com/elements")
driver.maximize_window()

#Interactuar con el desplegable
driver.find_element(By.CLASS_NAME, "icon").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "icon").click()
driver.find_element(By.ID, "item-0").click()
#Tiempo de espera
time.sleep(8)

#Cerrar el navegador 
driver.quit()