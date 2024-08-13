import random
rd = random.randint(1,100)
a = 1
b = 100
while True:
    try:
        guess = int(input(f"숫자 입력({a}~{b}):"))
        if guess<0 or guess > 100:
            print("입력 범위를 초과했어요")
        elif rd == guess:
            print("정답이에요!!")
            break
        elif rd > guess:
            print("랜덤수보다 작아요")
            a = guess
        else:
            print("랜덤수보다 커요")
            b = guess
    except ValueError:
        print("숫자만 입력 가능합니다.")