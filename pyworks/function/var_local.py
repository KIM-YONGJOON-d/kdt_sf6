# 지역 변수, 매개 변수
# 스택 구조
'''
total
num2
num1
'''
def calc():
    x = 2 * num1
    print("x=", x)

num1 = 10
num2 = 20
total = num1 + num2

calc()
