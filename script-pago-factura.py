from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

print("Accediendo a la página principal...")
driver.get("https://demo.guru99.com/telecom/index.html")

print("Haciendo clic en 'Pay Billing'...")
driver.find_element(By.LINK_TEXT, "Pay Billing").click()
time.sleep(2)

COMPRADOR_ID = "640079"  

driver.find_element(By.NAME, "customer_id").send_keys(COMPRADOR_ID)

driver.find_element(By.NAME, "submit").click()
time.sleep(2)

try:
    pay_button = driver.find_element(By.XPATH, "//input[@value='Pay']")
    pay_button.click()
    print("Factura pagada exitosamente.")
except:
    print("No hay factura para pagar o el ID es inválido.")

time.sleep(5)
driver.quit()
