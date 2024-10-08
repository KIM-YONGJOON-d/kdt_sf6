'''
유용한 문자열 함수
개수 - len(), 중복된 문자 개수 - 문자열.count()
대문자 변환 - 문자열.upper(), 소문자 - 문자열.lower()
문자열을 잘라서 리스트로 반환 - 문자열.split(구분기호)
'''
f = "바나나"
print(len(f))
print(len("banana"))

dupl_count = "banana"
print(dupl_count.count('a'))

upper_case = "Hello".upper()
lower_case = "Hello".lower()
print(upper_case, lower_case)

friends = "존 루나 제리"
print(friends.split())

alpha = "a:b:c:d"
print(alpha.split(':'))

email = "codingOn@spreatics.com"
print(email.split('@'))

msg = "Hello Python"
print(msg.replace('Python', 'C++'))