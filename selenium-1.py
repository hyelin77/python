# 터미널에서 설치 : pip install selenium
from selenium import webdriver
import time

#크롬 브라우저 실행
driver=webdriver.Chrome()
# 접속할 주소
driver.get("https://www.naver.com")
# 5초동안 현재상태에서 대기
time.sleep(5)