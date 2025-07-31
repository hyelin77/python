from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def scroll_fun():
    while True:
        h1=driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        time.sleep(2)
        h2=driver.execute_script("return document.documentElement.scrollHeight")

        if h1==h2:
            break

driver=webdriver.Chrome()
driver.get("https://www.youtube.com/")

time.sleep(2)
search_input=driver.find_element(By.CSS_SELECTOR, 'input[name="search_query"]')

search_input.send_keys("데몬헌터스")
search_input.send_keys(Keys.RETURN)

scroll_fun()

titles=driver.find_elements(By.XPATH, '//*[@id="video-title"]')

title_list=[]

for title in titles:
    if title.get_attribute("aria-rabel") and title.text:
        title_list.append(title.text)

c_result={
    "title":title_list,
}

result=pd.DataFrame(c_result)
result.to_csv("./result.csv", encoding="utf-8-sig")

result.sort_values(by=["title"], ascending=False).to_csv("./result2.csv", encoding="utf-8-sig")