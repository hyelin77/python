from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("")
time.sleep(3)

web_class=driver.find_elements(By.CLASS_NAME, )

for c in web_class:
    print(c.text)
print(len(web_class))