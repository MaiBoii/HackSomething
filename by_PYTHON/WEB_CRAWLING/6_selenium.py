from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image

url = "https://shop.hakhub.net/product/flying-ninja/"

service = Service(executable_path=r'/usr/bin/chromedriver')
options=webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080")
options.add_argument("lang=ko_KR")


driver=webdriver.Chrome(service=service,options=options)
driver.get(url)
driver.implicitly_wait(5)
driver.get_screenshot_as_file("닌자_옷.png")

Image.open("닌자_옷.png").convert("RGB").save("닌자_옷.png",quality=100)
im=Image.open("닌자_옷.png")
cropped_img =  im.crop((280,300,1100,780))
cropped_img.save("web_cropped.jpg", quality=100)

driver.close()