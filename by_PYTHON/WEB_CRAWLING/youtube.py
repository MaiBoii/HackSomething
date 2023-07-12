from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import warnings 
warnings.filterwarnings('ignore')

service = Service(executable_path=r'/usr/bin/chromedriver')
options=webdriver.ChromeOptions()
options.add_argument("lang=ko_KR")
driver=webdriver.Chrome(service=service,options=options)

url = 'https://www.youtube.com/watch?v=yQ20jZwDjTE&t=8040s'

driver.get(url)
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.5)

        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

time.sleep(1)

html_source = driver.page_source
soup = BeautifulSoup(html_source, "html.parser")