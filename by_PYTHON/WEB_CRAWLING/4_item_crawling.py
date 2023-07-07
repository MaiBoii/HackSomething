import requests 
from bs4 import BeautifulSoup

url = "https://shop.hakhub.net/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
elem_li = soup.find_all("li", {"class":"product"})

for index, li in enumerate(elem_li):
    print(f"\n======={index+1}번 상품=======")
    print('상품명:' ,li.find("h2", {"class":"woocommerce-loop-product__title"}).text)
    price = li.find("span", {"class":"price"}).text
    print('가격:',price.split(' ')[-1])
    try:
        print('평점 :',li.find("strong", {"class":"rating"}).text)
    except Exception as e:
        print('평점 정보가 없어요')