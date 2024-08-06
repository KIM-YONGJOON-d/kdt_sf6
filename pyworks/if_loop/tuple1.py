# 튜플(tuple) - 소괄호, 읽기 전용(수정, 삭제 안됨)
t1 = (10, 20 ,30)

print(t1)
print(type(t1))

print(t1[0])
print(t1[1:3])

# 수정 안됨
# t1[1] = 50

#삭제 안됨
# del t1[2]

# 요소를 1개 생성할 때 쉼표를 넣어줌
t3 = (7,)
print(t3)
print(type(t3))

# 튜플 요소의 합계
print(sum((10, 20, 30)))

# 튜플 요소의 최소값
print(min((10, 20, 30)))

# 튜플 합하기
tu1 = (1, 2, 3)
tu2 = (4, )
tu3= tu1+tu2
print(tu3)
print(tu3[0:])
print(tu3[:])
print(tu3[:-1])