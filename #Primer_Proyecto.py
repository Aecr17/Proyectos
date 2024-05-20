

#Youtube_Prueba_busqueda
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.youtube.com")
driver.maximize_window()
driver.find_element(By.NAME, "search_query").click()
driver.find_element(By.NAME, "search_query").send_keys("MLB")
driver.find_element(By.ID, "search-icon-legacy").click()
import time 
time.sleep(5)

driver.quit()

