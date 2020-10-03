# 크롤링 결과를 엑셀파일에 저장하기 위해
# File > Settings > + > openpyxl 다운로드
from openpyxl import Workbook

from bs4 import BeautifulSoup
from selenium import webdriver

# selenium으로 크롬을 열어서
driver = webdriver.Chrome('chromedriver')

# 네이버에서 '추석' 검색화면
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
# driver가 가져온 html들을 soup에 담는다.
soup = BeautifulSoup(req, 'html.parser')

# 기사 스크래핑 코드

# 기사 타이틀 우클릭 > 검사해서 활성화된 내용 copy>copy selector
# '#sp_nws1 > dl > dt > a'가 복사되었음
# articles=soup.select_one('#sp_nws1 > dl > dt > a') : 첫번째 기사 내용 가져오기
# print(articles.text) <- 기사의 제목만 출력하는 방법
# 두번째 기사는 '#sp_nws6 > dl > dt > a'로 보임
# 첫번째 기사는 sp_nws1, 두 번째 기사는 sp_nws6이기 때문에 규칙을 알 수 없다.
# 다른 방안이 필요하다.
# 기사 타이틀 우크릭 > 검사 눌러서 구조를 살펴 봐야한다.
# <li>들만 살펴보면 sp_nws1, sp_nws6, sp_nws9, sp_nws11, sp_nws14, ...

# <ul> 부분을 copy selector 가져와서 본다.
# 결과는 '#main_pack > div.news.mynews.section._prs_nws > ul' 이고
# '#main_pack > div.news.mynews.section._prs_nws > ul' 안에 있는 li들을 가져와라
articles=soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')


wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])



# 기사 제목, url 뽑아내기 + 신문사도 뽑아내기
for article in articles:

#     # article은 ul안의 각 li
# a의 출력 결과 : <a class="_sp_each_title" href="http://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002679690&amp;CMPT_CD=P0010&amp;utm_source=naver&amp;utm_medium=newsearch&amp;utm_campaign=naver_news" onclick="return goOtherCR(this, 'a=nws*j.tit&amp;r=20&amp;i=880000E3_000000000000000002286742&amp;g=047.0002286742&amp;u='+urlencode(this.href));" target="_blank" title="악몽 같던 1949년, 이 마을에 추석이 사라진 이유">악몽 같던 1949년, 이 마을에 <strong class="hl">추석</strong>이 사라진 이유</a>
     title=article.select_one('dl > dt > a').text # li안의 dl안의 dt안의 a를 뽑아낸 후 text만 또 뽑아낸다.
     url=article.select_one('dl > dt > a')['href']

# 신문사 뽑아내기
# 신문사 부분 우클릭 > 검사
# '<span class="_sp_each_source"> == $0' 부분을 copy selector 하면
# '#sp_nws6 > dl > dd.txt_inline > span._sp_each_source' 이렇게 나온다.

# 가져올 부분은 'span._sp_each_source'이든 'dl > dd.txt_inline > span._sp_each_source'이든 상관없음
#     comp=article.select_one('dl > dd.txt_inline > span._sp_each_source')
#     comp=article.select_one('span._sp_each_source')
# 이와 같이 출력됨 : <span class="_sp_each_source">세계일보<i class="sprenew api_ico_pick">언론사 선정</i></span>

# 신문사 이름만 뽑아내기 위해 .text 추가
#     comp=article.select_one('span._sp_each_source').text
# 이와 같이 출력됨 : 세계일보언론사 선정
# 뒤에 '언론사 선정'이라는 단어가 붙음

# ' ' 공백으로 나눈뒤 앞 부분만 갖고와서(split(' ')[0]
# 언론사라는 부분은 필요없다.(replace('언론사','')
     comp=article.select_one('dl > dd.txt_inline > span._sp_each_source').text.split(' ')[0].replace('언론사','')
# 이와 같이 출력됨 : 세계일보

# 기사 제목, url, 신문사 모두 출력
#     print(title, url, comp)

# 출력 대신 엑셀에 append 하기
     ws1.append([title, url, comp])

driver.quit()
wb.save(filename='articles.xlsx')
