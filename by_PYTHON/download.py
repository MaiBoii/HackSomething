import requests

def download(url, filename="downloaded_image.jpg"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ 이미지가 {filename} 로 저장되었습니다.")
    else:
        print(f"❌ 다운로드 실패: {response.status_code}")

download("https://m.dokidokigoods.co.kr/web/product/big/202309/4a1c76b90cbedb9baf4772f42bc60f69.jpg")
