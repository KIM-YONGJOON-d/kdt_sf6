# 실습1
student = {}
student = {'Alice' : 85, 'Bob' : 90, "Charlie" : 95 }

# 학생 추가
student["David"] = 80

# 학생 점수 수정
student["Alice"] = 88

# 학생 삭제
student.pop("Bob")

# 학생 전체 출력
for key in student:
    print(f'{key} : {student.get(key)}')