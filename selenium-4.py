from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.nate.com")
search_element=driver.find_element(By.XPATH, '//*[@id="q"]')

search_element.send_keys("수시 일정")

btn=driver.find_element(By.XPATH, '//*[@id="acBtn"]')
btn.click()

time.sleep(10)
