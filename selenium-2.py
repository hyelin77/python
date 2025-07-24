from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.example.com")

p_element=driver.find_element(By.TAG_NAME, 'p')
print("p 태그의 첫번째 요소만 가져옴")
print(p_element)


p_elements=driver.find_elements(By.TAG_NAME, 'p')
print(type(p_elements))

print("p 태그의 모든 요소 가져옴")
for p in p_elements:
    print(p.text)
 