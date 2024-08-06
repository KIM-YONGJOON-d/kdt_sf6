# 자료구조 - 딕셔너리(dictionary)
# "치킨" : "닭을 튀긴 요리", key(키): value(값)
# {} 중괄호 사용

# fruits = ['apple', 'banana', 'cherry']
fruits = {
    "apple": "사과",
    "banana": "바나나",
    "peach":"복숭아"
    }

print(fruits["apple"])
# print(fruits["toamto"])

print(fruits.get("banana"))
print(fruits.get("toamto"))

fruits["strawberry"] = "딸기"
print(fruits)
print(type(fruits))

fruits["peach"] = "천도 복숭아"
print(fruits)

fruits.pop("banana")
print(fruits)

# 키만 반환
print(fruits.keys())

# 값만 반환
print(fruits.values())

# 키와 값 모두 반환
print(fruits.items())

#키와 값 전체 조회
for key in fruits:
    print(key, ":", fruits[key])

# 딕셔너리 생성
dict1 = {1:'a', 2:'b', 3:'c'}
print(dict1)


# key = 4, value = 'd' 추가
dict1[4] = 'd'
print(dict1)

# for문을 이용한 전체 조회

for i in dict1:
    print(f'{i} : {dict1[i]}')

# 요소 수정 - key 3 을 'k'로 변경
dict1[3] = 'k'
print(dict1)

# 요소 삭제 - key 2 삭제
dict1.pop(2)
print(dict1)