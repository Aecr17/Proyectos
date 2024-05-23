# Librerias importadas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv


#Interactuar con la pagina web
driver=webdriver.Chrome()
driver.get("https://demoqa.com/elements")
driver.maximize_window()

#Interactua con un desplegable de una pagina 
dropdown =driver.find_element(By.CLASS_NAME, "icon").click()
time.sleep(2)
dropdown= driver.find_element(By.CLASS_NAME, "icon").click()

#Interacion con el boton "Caja de texto"
btn_caja_texto = driver.find_element(By.ID, "item-0")
btn_caja_texto.click()

#Aca podemos interactuar con datos en la caja de texto de la pagina
text_username = driver.find_element(By.ID, "userName").send_keys("Andres") 
text_email = driver.find_element(By.ID, "userEmail").send_keys("Andres@prueba.com")
text_currentAddress = driver.find_element(By.ID, "currentAddress").send_keys("Av Prueba 5500")
text_permanetAdderss = driver.find_element(By.ID, "permanentAddress").send_keys("Av Prueba 5500"+Keys.TAB)
btn_send = driver.find_element(By.ID, "submit")
btn_send.click()
time.sleep(2)

#Aca podemos interactuar con las Web tables
web_tables = driver.find_element(By.ID, "item-3")
web_tables.click()
add = driver.find_element(By.ID, "addNewRecordButton")
add.click()
#registration_form = driver.find_element(By.XPATH, '//*[@id="submit"]')
#registration_form.click()
time.sleep(2)

#Aca interactuamos con el modulo web tables
first_name_text = driver.find_element(By.ID, "firstName")
first_name_text.send_keys("Andres")
last_name_text = driver.find_element(By.ID, "lastName")
last_name_text.send_keys("Cardoza")
email_text = driver.find_element(By.ID, "userEmail")
email_text.send_keys("prueba@gmail.com")
age_text = driver.find_element(By.ID, "age")
age_text.send_keys("23")
salary_text = driver.find_element(By.ID, "salary")
salary_text.send_keys("80")
department_text = driver.find_element(By.ID, "department")
department_text.send_keys("17")
time.sleep(2)
registration_form = driver.find_element(By.XPATH, '//*[@id="submit"]')
registration_form.click()
#text_asercion = "Campos Vacios no se puede avanzar:"
#assert "Acceso incorrecto" == registration_form.text,"Los campos son obligatorios"

#Tiempo de espera
time.sleep(8)

#Cerrar el navegador 
driver.quit()
