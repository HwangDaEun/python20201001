from openpyxl import Workbook

# workbook 하나 만들기
wb = Workbook()

ws1 = wb.active

# 시트 제목을 articles로 하기
ws1.title = "articles"

# 첫째줄은 이 내용으로
ws1.append(["제목", "링크", "신문사"])

# 둘쨰줄은 이 내용으로
ws1.append(["제목", "링크", "신문사"])

# 저장
wb.save(filename='articles.xlsx')
