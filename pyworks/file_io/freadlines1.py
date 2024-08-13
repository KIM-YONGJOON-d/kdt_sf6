f = open("./source/season.txt", "r")
seasons = f.readlines()
try:
    print(seasons[1])
    f.close()
except FileExistsError:
    print("파일을 찾을 수 없습니다")