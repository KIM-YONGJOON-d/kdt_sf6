# 별 찍기
'''
for i in range(1, 5):
    print("*" * i)

print("=" * 20)

# 공백이 먼저인 직각삼각형
for i in range(1, 5):
    print(" " * (4-i) + "*" * i)

'''
a = int(input("몇 줄? > "))
for i in range(1, a+1):
    print("*" * i)

b = int(input("몇 줄? > "))
for i in range(1, b+1):
    print(" " * (b-i) + "*" * i)

c = int(input("몇 줄? > "))
for i in range(1, c+1):
    print(" " * ((c-i)//2) + "*" * i + " " * ((c-i)//2))

input_num = input("숫자 입력:").split(" ")
print(input_num)
numbers = []
for i in input_num:
    numbers.append(int(i))
print(numbers)


