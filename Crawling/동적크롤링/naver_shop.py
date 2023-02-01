from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 

chrome = webdriver.Chrome("Crawling/동적크롤링/chromedriver.exe", options=options)
chrome.get("https://shopping.naver.com/")
wait = WebDriverWait(chrome, 10)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "input[class=_searchInput_search_text_fSuJ6]")
search.send_keys("아이폰 케이스")
time.sleep(4)

button = find(wait, "._searchInput_button_search_h79Dk")
button.click()
time.sleep(4)

chrome.close()
