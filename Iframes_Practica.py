#Librerias importadas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Instanciamos el driver de Chrome
driver = webdriver.Chrome()

# Navegar a una URL
driver.get("https://practice-automation.com/iframes/")

# Maximizar ventana
driver.maximize_window()

# se localiza el iframe
iframe = driver.find_element(By.ID,"frame2")
driver.switch_to.frame(iframe)

## Espera explicita de 3 segundos
#driver.implicitly_wait(4)
espera_explicita = WebDriverWait(driver,3) 

## INTERACTUA CON EL BOTON DE SALIDA
exit_click = driver.find_element (By.CLASS_NAME, "ab-close-button")
exit_click.click()

#Otra forma de interactuar con la ventana de espera 
# button_ok = driver.find_element(By.CLASS_NAME, "ab-message-button")
# button_ok.click()

#Se agrega time sleep para observar la interaccion con el botton login
time.sleep(3)

#Interaccion con el boton de Login dentro del iframe
boton_dentro_del_iframe = driver.find_element(By.XPATH,'//*[@id="fitt-analytics"]/div[2]/div/div/div/div/nav/ul/li[1]/div/div/button')
boton_dentro_del_iframe.click()
driver.switch_to.default_content()
time.sleep(10)
