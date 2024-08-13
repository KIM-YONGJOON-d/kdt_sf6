# 파일 쓰기 - 파일을 생성
# 파일 열기(open()) > 파일 쓰기(write()) > 파일 닫기(close())
# 절대 경로, 상대 경로
# 모드 - 쓰기모드 'w', 읽기 모드 "r", 추가 모드 "a"

f = open("c:/pyfile/file1.txt", "w")
f.write("Hello python\n")
f.write("너무 더워")
f.write("100")
f.close()
