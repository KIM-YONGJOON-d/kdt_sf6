# 과제 1

# vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
# while True:
#     print("=============== RESTART")
#     drink = input("마시고 싶은 음료? ")
#     if drink in vending_machine:
#         print(f"{drink}드릴게요")
#         vending_machine.remove(drink)
#         print('남은 음료는', vending_machine)
#     else:
#         print(f'{drink}는 지금 없네요')


# 과제 2
vending_machine = ['게토레이', '레쓰비', '게토레이', '생수', '이프로', '생수']

while True:
    who = input("사용자 종류를 입력하세요: \n1.소비자 \n2.주인 ")

    if who == '1':
        drink = input("마시고 싶은 음료? ")
        if drink in vending_machine:
            print(f"{drink} 드릴게요.")
            vending_machine.remove(drink)
            print('남은 음료는', vending_machine,'\n')
        else:
            print(f'{drink}는 지금 없네요.\n')

    elif who == '2':
        todo = input('할 일 선택 (1.추가, 2.삭제): ')

        if todo == '1':
            print('남은 음료는', vending_machine)
            drink = input("추가할 음료수? ")
            vending_machine.append(drink)
            vending_machine.sort()
            print("추가 완료.")
            print("남은 음료는", vending_machine,'\n')

        elif todo == '2':
            print("남은 음료는", vending_machine)
            drink = input("삭제할 음료수?: ")
            if drink in vending_machine:
                vending_machine.remove(drink)
                print("삭제 완료.")
                print("남은 음료는", vending_machine,'\n')
            else:
                print(f"{drink}는 목록에 없습니다.\n")

    else:
        print("1 또는 2로 입력해주세요.\n")
        continue

