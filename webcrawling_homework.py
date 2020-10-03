import dload

from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%B3%91%EC%95%84%EB%A6%AC+%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails=soup.select('#imgList > div > a > img')

i=1
for thumbnail in thumbnails:
    img=thumbnail['src']
    dload.save(img,f'imgs_homework/chick{i}.jpg')
    i+=1


driver.quit() # 끝나면 닫아주기
