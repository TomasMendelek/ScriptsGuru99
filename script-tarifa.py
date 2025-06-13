from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.guru99.com/telecom/index.html")

driver.find_element(By.LINK_TEXT, "Add Tariff Plan").click()
time.sleep(4)


driver.find_element(By.ID, "rental1").send_keys("200")
time.sleep(2)
driver.find_element(By.ID, "local_minutes").send_keys("1000")
time.sleep(2)
driver.find_element(By.ID, "inter_minutes").send_keys("500")
time.sleep(2)
driver.find_element(By.ID, "sms_pack").send_keys("100")
time.sleep(2)
driver.find_element(By.ID, "minutes_charges").send_keys("1")
time.sleep(2)
driver.find_element(By.ID, "inter_charges").send_keys("5")
time.sleep(2)
driver.find_element(By.ID, "sms_charges").send_keys("0.5")

driver.find_element(By.NAME, "submit").click()

time.sleep(5) 

driver.quit()
