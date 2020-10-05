# 텍스트 파일 쓰기 뼈대

f = open("test.txt", "w", encoding="utf-8")

for i in [1,2,3,4,5,6,7,8,9,10]:
    f.write(f"{i}번째 줄입니다.\n")
f.close()

# 텍스트 파일 읽기 뼈대

text=''
#with open 구문은 아래 내용이 끝나면 open한 파일을 닫는다.
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines() # 파일을 한줄씩 읽는다.
    for line in lines:
        text+=line

print(text)
