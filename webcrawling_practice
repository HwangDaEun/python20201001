# File > Settings > Project:{프로젝트명} > Python Interpreter
# 우측에 '+' 눌러서 dload -> selenium -> bs4 순으로 다운로드

import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 셀레니움 웹드라이버 설치 링크
# 주소 입력창 오른쪽에 있는 세소로 점 3개 있는 버튼 클릭 후 아래 도움말(E) 클릭
# Chromw 정보에서 Chrome 버전 확인 후 아래 링크에서 버전에 맞는 드라이버 설치
# https://chromedriver.storage.googleapis.com/index.html?path=85.0.4183.87/
# 설치 후 압축 풀어서 프로젝트 폴더에 드라이버 프로그램 저장하기

# 드라이버 가져오기
driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
# 다음에서 아이유 검색 화면
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")

time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source

# BeautifulSoup을 통해 필요한 내용을 쉽게 솎아낼 수 있게 만들기
soup = BeautifulSoup(req, 'html.parser')

# 이미지 우클릭 후 맨아래 검사 누름, 활성화된 내용에 우클릭 하여 copy> copy selector
# '#imgList > div:nth-child(1) > a > img'가 복사되어 있음
# 다음 이미지는 #imgList > div:nth-child(2) > a > img
# 모든 이미지를 가리키기 위해서 div:nth-child(1)에서 div로 지칭함
thumbnails=soup.select('#imgList > div > a > img')

i=1
for thumbnail in thumbnails:
    img=thumbnail['src']
    dload.save(img,f'img/{i}.jpg') # 1.jpg, 2.jpg로 저장될 수 있게 하기
    i+=1

driver.quit() # 끝나면 닫아주기
