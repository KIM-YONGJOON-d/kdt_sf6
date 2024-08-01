# 실습 1
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")
print(f'안녕하세요! {name}님 ({age}세)')

# 실습 2
try:
    name = input("이름을 입력하세요.")
    year1 = int(input("태어난 년도를 입력하세요."))
    year2 = int(input("올해 년도를 입력하세요."))
    print(f'올해는 {year2}년, {name}님의 나이는 {year2-year1+1}세입니다.')
except:
    print("숫자를 입력해주세요")

