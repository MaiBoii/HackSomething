import requests
import asyncio
import aiohttp
import json
from time import time
from bs4 import BeautifulSoup

page_url = ["https://shop.hakhub.net/page/1/", "https://shop.hakhub.net/page/2/"]
json_path="./comments.json"

#일단 모든 상품의 url을 싹 가져오자
def get_product_urls(urls):
    product_urls=[]
    for url in urls:
        r=requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        elem_li = soup.find_all("li", {"class":"product"})
        for li in elem_li:
            product_urls.append(li.find("a")["href"])
    print(f"{len(product_urls)} 개의 상품이 존재합니다.")
    return product_urls

#같은 TCP 세션을 사용하게끔 통일시키기
#동일 대상에 대한 동시 연결을 제한한다.(기본값이 0=무제한인데 서버에 과부하 줄 수도 있음)
async def async_func(urls):
    conn = aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=conn) as s:
        futures=[asyncio.create_task(show_product_review(s,url)) for url in urls]
        results=await asyncio.gather(*futures)
    with open(json_path, "w", encoding="utf-8") as f:
        print(f"JSON file save as: {json_path}")
        json.dump(results, f, indent=4, ensure_ascii=False)

#리뷰들을 json 파일로 가져오기 
#aiohttp 모듈의 세션을 생성, 비동기로 이용. 
async def show_product_review(s, url):
    async with s.get(url) as r:
        html=await r.text()
    soup=BeautifulSoup(html, 'html.parser')
    product_name=soup.find("h1").text
    comments=soup.find_all("div", {"class":"comment-text"})
    comment_dict={}
    comment_dict["product_name"]=product_name
    comment_array=[]
    for comment in comments:
        comment_array.append(
            #댓글 json 양식 작성
            {
                "author":comment.find(
                    "strong",{"class":"woocommerce-review__author"}
                ).text,
                "rating": comment.find("strong", {"class":"rating"}).text,
                "datetime":comment.find("time")["datetime"],
                "description":comment.find("div", {"class":"description"}).text
            }
        )
    comment_dict["comments"]=comment_array
    return comment_dict

if __name__ == "__main__":
    begin=time()
    product_urls=get_product_urls(page_url)
    asyncio.run(async_func(product_urls))
    end=time()
    print(f"실행 시간: {end - begin}")