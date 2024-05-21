# Librerias importadas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Interactuar con la pagina web
driver=webdriver.Chrome()
driver.get("https://demoqa.com/elements")
driver.maximize_window()
# se agrega un nuevo time sleep
time.sleep(2)
#Interactua con un desplegable de una pagina 
driver.find_element(By.CLASS_NAME, "icon").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "icon").click()
driver.find_element(By.ID, "item-0").click()

#Aca podemos interactuar con datos en la caja de texto de la pagina
driver.find_element(By.ID, "userName").send_keys("Andres")
driver.find_element(By.ID, "userEmail").send_keys("Andres@prueba.com")
driver.find_element(By.ID, "currentAddress").send_keys("Av Prueba 5500")
driver.find_element(By.ID, "permanentAddress").send_keys("Av Prueba 5500"+Keys.TAB)
driver.find_element(By.ID, "submit").click()
#Tiempo de espera
time.sleep(8)

#Cerrar el navegador 
driver.quit()