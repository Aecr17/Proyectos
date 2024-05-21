

#Youtube_Prueba_busqueda
#Se actualiza para probar github
from selenium.webdriver.common.by import By
from selenium import webdriver
import time 
driver=webdriver.Chrome()
driver.get("https://www.youtube.com")
driver.maximize_window()
driver.find_element(By.NAME, "search_query").click()
driver.find_element(By.NAME, "search_query").send_keys("MLB")
driver.find_element(By.ID, "search-icon-legacy").click()

time.sleep(5)

driver.quit()

