from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.guru99.com/telecom/index.html")

driver.find_element(By.LINK_TEXT, "Add Tariff Plan to Customer").click()
time.sleep(2)


COMPRADOR_ID = "640079"  
driver.find_element(By.ID, "customer_id").send_keys(COMPRADOR_ID)

driver.find_element(By.NAME, "submit").click()
time.sleep(2)

print("Seleccionando un plan tarifario y confirmando...")
try:
    driver.find_element(By.NAME, "tariff_plan").click()
    driver.find_element(By.NAME, "submit").click()
    print("Plan agregado correctamente.")
except:
    print("No se encontró un plan disponible o el Customer ID no es válido.")

time.sleep(5)
driver.quit()
