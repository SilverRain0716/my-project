from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

chrome = webdriver.Chrome("Crawling/동적크롤링/chromedriver.exe")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com/home")
# login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "gnb_login_button")))
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "gnb_login_li")))
print(login_button)
login_button.click()

time.sleep(3)
chrome.close

