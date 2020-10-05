# File > Settings > Python interpreter에서 wordcloud 다운로드
from wordcloud import WordCloud

from PIL import Image
import numpy as np

# 데이터 클렌징 작업 전
# text=''
# with open("kakaotalk.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines() # 파일을 한줄씩 읽는다.
#     for line in lines:
#         text+=line

# 워드클라우드를 구름모양으로 보기위한 구름모양 이미지 링크
# https://s3.ap-northeast-2.amazonaws.com/materials.spartacodingclub.kr/free/cloud.png

# 데이터 클렌징 작업
text=''
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()               # 파일을 한줄씩 읽는다.
    for line in lines[5:]:              # 다섯 번째줄 부터 읽겠다.
        if '] [' in line:               # 시스템 메시지 제외
            # text+=line.split('] ')[2] # 대화 내용만 보기
            text += line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('이모티콘\n','').replace('사진\n','').replace('삭제된 메시지입니다','').replace('https','') # 제외할 문자 제외



# 마스킹된 워드 클라우드 만들기
# # font_path 변수에 아까 검색한 폰트 경로 입력
# # 이때, Windows는 '\'(역슬래시)를 '/'(슬래시)로 변경해주어야 한다.
mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/Hancom Gothic Bold.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")
