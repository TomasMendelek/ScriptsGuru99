from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.guru99.com/telecom/index.html")

driver.find_element(By.LINK_TEXT, "Add Customer").click()
time.sleep(2)

driver.find_element(By.XPATH, "//label[text()='Done']").click()

driver.find_element(By.ID, "fname").send_keys("Tomas")
time.sleep(1)

driver.find_element(By.ID, "lname").send_keys("Corbalan Mendelek")
time.sleep(1)

driver.find_element(By.ID, "email").send_keys("tomascorbalanmendelek@gmail.com")
time.sleep(1)

driver.find_element(By.NAME, "addr").send_keys("Urquiza 939")
time.sleep(1)

driver.find_element(By.ID, "telephoneno").send_keys("3865454647")
time.sleep(1)


driver.find_element(By.NAME, "submit").click()

time.sleep(5)

driver.quit()
