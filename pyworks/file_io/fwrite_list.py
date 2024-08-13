# 리스트 자료 쓰기
# source 폴더 - 나를 기준으로
# 점한개 슬래시(./), 상위 계층이면 (../)
f = open("./source/season.txt", "w")
season = ["봄", "여름", "가을", "겨울"]
for i in season:
    f.write(i + '\n')

f.close()

f = open("./source/season.txt", "r")
data = f.read()
print(data)
f.close()
