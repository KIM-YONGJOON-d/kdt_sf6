
# if문 - 조건: 나이가 15세 이상이면 "관람가"라고 출력

age = 14
"""
if age>=15:
    print("관람가")
print(f'나이는 {age}세 입니다.')
"""

if age>=15:
    print("관람가")
else:
    print("관람불가")
print(f'나이는 {age}세 입니다.')

# 어떤 수를 짝수인지 홀수인지 판별하는 프로그램
num= int(input("수를 입력하세요 :"))
if num%2==0:
    print(f"{num}은 짝수다")
else:
    print(f"{num}은 홀수다")
