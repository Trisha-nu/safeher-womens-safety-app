from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/trish/OneDrive/Desktop/SafeHer/safeher-womens-safety-app/frontend/index.html")

time.sleep(2)

button = driver.find_element(By.TAG_NAME, "button")

button.click()

time.sleep(5)

driver.quit()