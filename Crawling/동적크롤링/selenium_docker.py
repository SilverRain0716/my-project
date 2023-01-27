# 크롬드라이버 파일과 파이썬 파일을 같은 폴더에 두어야 함

from selenium import webdriver
import time

browser = webdriver.Chrome("Crawling/동적크롤링/chromedriver.exe")
browser.get("http://naver.com")
time.sleep(10)
browser.close()

# docker로 실행하는 방법
# docker run -p 4444:4444 selenium/standalone-chrome -> 터미널로 실행
'''
browser = webdriver.remote("ip주소:4444/wd/hub", DesiredCapabilities.CHROME)
browser.get("http://naver.com")
print(browser.title)
browser.close()
'''

