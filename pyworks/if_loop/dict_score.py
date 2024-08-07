# 학생 3명의 성적 통계
student = [
    {"name": "이대한", "kor" : 90, "math" : 85},
    {"name": "박민국", "kor" : 80, "math" : 75},
    {"name": "윤지능", "kor" : 95, "math" : 90},
]
print("♣ 개인별 평균 점수 ♣")
print(" 이름  국어 수학 평균")

for std in student:
    avg = (std["kor"] + std["math"])/2
    print(f'{std["name"]}  {std["kor"]}  {std["math"]}  {avg:.1f}')

print("♣ 과목별 총점, 평균 ♣")
kor_total = 0
math_total = 0
for i in student:
    kor_total += i["kor"]
    math_total += i["math"]
print(f'국어 총점: {kor_total}')
print(f'수학 총점: {math_total}')
print(f'국어 평균: {kor_total/len(student):.2f}')
print(f'국어 평균: {math_total/len(student):.2f}')