# Librerias importadas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Interactuar con la pagina web
driver=webdriver.Chrome()
driver.get("https://demoqa.com/elements")
driver.maximize_window()

#Interactua con un desplegable de una pagina 
dropdown =driver.find_element(By.CLASS_NAME, "icon").click()
time.sleep(2)
dropdown= driver.find_element(By.CLASS_NAME, "icon").click()
btn_caja_texto = driver.find_element(By.ID, "item-0")
btn_caja_texto.click()

#Aca podemos interactuar con datos en la caja de texto de la pagina
text_username = driver.find_element(By.ID, "userName").send_keys("Andres")
text_email = driver.find_element(By.ID, "userEmail").send_keys("Andres@prueba.com")
text_currentAddress = driver.find_element(By.ID, "currentAddress").send_keys("Av Prueba 5500")
text_permanetAdderss =driver.find_element(By.ID, "permanentAddress").send_keys("Av Prueba 5500"+Keys.TAB)
btn_send = driver.find_element(By.ID, "submit")
btn_send.click()

#Tiempo de espera
time.sleep(8)

#Cerrar el navegador 
driver.quit()