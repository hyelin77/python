#크롤링(crawling)은 웹페이지를 가져와서 거기서 데이터를 추출해 내는 행위
#selenium: 동적 크롤링
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.naver.com")

login_button=driver.find_element(By.XPATH, '//*[@id="account"]/div/a')

login_button.click()

time.sleep(10)