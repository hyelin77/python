from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://search.danawa.com/dsearch.php?query=%EC%95%84%EC%9D%B4%ED%8C%A8%EB%93%9C&originalQuery=%EC%95%84%EC%9D%B4%ED%8C%A8%EB%93%9C&checkedInfo=N&volumeType=allvs&page=1&limit=40&sort=saveDESC&list=list&boost=true&tab=main&addDelivery=N&coupangMemberSort=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=122579&defaultPhysicsCategoryCode=224%7C38768%7C53984%7C0&defaultVmTab=7251&defaultVaTab=1072144&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A")

notebook_names=driver.find_elements(By.CLASS_NAME, 'prod_name')

for name in notebook_names:
    print(name.text)

time.sleep(10)