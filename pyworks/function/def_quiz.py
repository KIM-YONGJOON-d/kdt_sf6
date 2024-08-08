# 실습 1
# def abc(x, y):
#     if x == y:
#         return x * y
#
#     else:
#         return x + y
# print(f'결과(곱): {abc(2,2)}')
# print(f'결과(합): {abc(2,3)}')

# 실습 4
# def times3():
#     count =0
#     for i in range(1, 31):
#         if i % 3 == 0:
#             count += 1
#             print(i,end=' ')
#     print(f'\n3의 배수의 개수 :{count}')
#
# times3()

# 실습 3

vending_machine = ['게토레이', '레쓰비', '게토레이', '생수', '이프로', '생수']

def check_machine():
 vending_machine.sort()
 print("남은 음료수는",vending_machine)

def is_drink(drink):
 if drink in vending_machine:
  print(f"{drink}는(은) 있습니다.")
 else:
  print(f"{drink}는(은) 없습니다.")
def add_drink(drink):
 vending_machine.append(drink)
 vending_machine.sort()
 print(f"남은 음료수는 {vending_machine}")
def remove_drink(drink):
 vending_machine.remove(drink)
 vending_machine.sort()
 print(f"남은 음료수는 {vending_machine}")

check_machine()
is_drink('게토레이')
add_drink('오렌지 주스')
remove_drink('게토레이')
# while True:
#     who = input("사용자 종류를 입력하세요: \n1.소비자 \n2.주인 ")
#
#     if who == '1':
#         drink = input("마시고 싶은 음료? ")
#         if drink in vending_machine:
#             print(f"{drink} 드릴게요.")
#             vending_machine.remove(drink)
#             print('남은 음료는', vending_machine,'\n')
#         else:
#             print(f'{drink}는 지금 없네요.\n')
#
#     elif who == '2':
#         todo = input('할 일 선택 (1.추가, 2.삭제): ')
#
#         if todo == '1':
#             print('남은 음료는', vending_machine)
#             drink = input("추가할 음료수? ")
#             vending_machine.append(drink)
#             vending_machine.sort()
#             print("추가 완료.")
#             print("남은 음료는", vending_machine,'\n')
#
#         elif todo == '2':
#             print("남은 음료는", vending_machine)
#             drink = input("삭제할 음료수?: ")
#             if drink in vending_machine:
#                 vending_machine.remove(drink)
#                 vending_machine.sort()
#                 print("삭제 완료.")
#                 print("남은 음료는", vending_machine,'\n')
#             else:
#                 print(f"{drink}는 목록에 없습니다.\n")
#
#     else:
#         print("1 또는 2로 입력해주세요.\n")
#         continue


