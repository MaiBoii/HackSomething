import requests

url = "https://shop.hakhub.net"
r=requests.get(url)
print(f'상태 코드는: \n{r.status_code}')
print(f'응답 헤더는: \n{r.headers}')
print("응답 바디: ")
print(r.text[:1000])
