# 입력 함수 - input(문자열)
#name = input("이름입력 : ")
#print("당신의 이름은 " + name + "입니다")

#number = input("숫자 입력 : ")
#print(int(number) + 1)

try:
    num1 = int(input("첫번째 수 입력: "))
    num2 = int(input("두번째 수 입력: "))
    print(num1+num2)
except:
    print("정수를 입력해주세요")

