# 바이너리 파일(binary file)읽고 쓰기
# 모드 - 쓰기"wb", 읽기 "rb"
# 바이너리 기계어로 변환하는 함수 - encode
# 기계어를 텍스트로 변환하는 함수 - decode



with open("./output/data.bin", "wb") as f:
    txt = "드론이 날아간다."
    f.write(txt.encode())

with open("./output/data.bin", "rb") as f2:
    data = f2.read()
    print(data)
    print(data.decode())