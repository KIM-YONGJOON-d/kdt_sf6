# 변수
# 자료형(type) - 숫자(정수, 실수), 문
floor = 3 # 정수를 저장하는 floor라는 변수
name = "김용준"
weight = 2.5

#print("나는 ", floor, "층에 살아요", sep='')
print(f'나는 {floor}층에 살아요')
print("내 이름은 " + name + "입니다")
#print("이 노트북의 무게는 " + str(weight) + "kg입니다")
print(f"이 노트북의 무게는 {weight}kg입니다")

# type(자료형) - 자료형을 인식하는 함수
# int - 정수(integer), float - 실수(부동)
# str - 문자열(string)
# str()자료형 변환 
print(type(floor))
print(type(weight))
print(type(name))
