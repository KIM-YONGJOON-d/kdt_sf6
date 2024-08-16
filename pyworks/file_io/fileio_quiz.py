#
# f = open("c:/pyfile/gugudan.txt", "w")
# for i in range(2,10):
#     for j in range(1,10):
#         a = f"{i} x {j} = {i*j}\n"
#         f.write(a)
# f.close()
#
# f = open("c:/pyfile/gugudan.txt", "r")
# print(f.read())
# f.close()

# 실습2
# try:
#     with open("./source/member.txt", 'w') as f:
#         for i in range(3):
#             name = input("이름을 입력하세요: ")
#             pw = input("비밀번호를 입력하세요: ")
#             f.write(f'{name} {pw}\n')
#
    # with open("./source/member.txt", 'r') as f:
    #     print(f.read())
# except FileNotFoundError:
#     print("파일을 찾을 수 없습니다.")

# 실습3
name = input('이름 입력: ')
pw = input('비밀번호 입력: ')
user = name + " " + pw + "\n"

with open("./source/member.txt", 'r') as f:
    member_list = f.readlines()
    sw = False
    for member in member_list:
        if member == user:
            sw = True
    if sw:
        print('로그인 성공!')
    else:
        print('로그인 실패!')