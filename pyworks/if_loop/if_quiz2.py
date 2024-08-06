# 다중 if 실습
while True:
    score = int(input("점수 입력 : "))
    if score < 0 or score > 100:
        print("올바른 점수를 입력해주세요.")
        continue
    elif score >= 90:
        print("A 등급입니다.")
        break
    elif score >=80:
        print("B 등급입니다.")
        break
    elif score >=70:
        print("C 등급입니다.")
        break
    elif score >=60:
        print("D 등급입니다.")
        break
    else:
        print("E 등급입니다.")
        break





