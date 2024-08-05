# 다중 조건문

'''
age = 25
if age < 20 and age >= 0:
    print("미성년자 입니다.")
elif age<30:
    print("20대 입니다.")
elif age<40:
    print("30대 입니다.")
else:
    print("이제는 중년...")
print(f"나이는 {age}세 입니다.")
'''

# 연령이 20인 경우 성별이 여이면 "20대 여성입니다"로 출력하고
# 남이면 "20대 남성입니다"로 출력하세요
age = int(input("나이를 입력하세요: "))
gender = ""
if age < 20 and age >= 0:
    print("미성년자 입니다.")
elif age<30:
    gender = input("여 or 남으로 입력해주세요: ")
    if gender =="여":
        print("20대 여성입니다.")
    else:
        print("20대 남성입니다")
elif age<40:
    gender = input("여 or 남으로 입력해주세요: ")
    if gender == "여":
        print("30대 여성입니다.")
    else:
        print("30대 남성입니다")
else:
    print("이제는 중년...")
print(f"나이는 {age}세 입니다.")