from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") # 먹통이 되었을 때 사용
# options.add_argument("headless") # 창을 안뜨게 하는 것

chrome = webdriver.Chrome("Crawling/동적크롤링/chromedriver.exe", options=options)
chrome.get("https://shopping.naver.com/")
WebDriverWait(chrome, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "input[name=query]"))
chrome.close()


# chrome.back()
# chrome.forward()
# time.sleep(10)