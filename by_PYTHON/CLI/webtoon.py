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

f= open("./외지주_전체_회차.txt", "a", encoding='utf-8')
page_num = 1
while True:
    url = f'https://comic.naver.com/webtoon/list?titleId=641253&page={page_num}'
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
    first_title = soup.find_all("span", attrs={"class":"EpisodeListUser__text--gj_xm"})[1].get_text()
    webtoon_titles = soup.find_all("span", attrs={"class":"EpisodeListList__title--lfIzU"})
    for title in webtoon_titles:
        f.write(title.get_text()+'\n')
    if webtoon_titles[-1].get_text() == first_title:
        break
    page_num += 1
f.close()
