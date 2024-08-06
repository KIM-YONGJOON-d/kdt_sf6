# 자료구조 - set - {}
# 중복이 안됨, 순서가 없다(인덱싱 안됨)

# cart = ["양파", "쌀", "콩나물", "쌀"]
# print(cart)

cart = {"양파", "쌀", "콩나물", "쌀"}
print(cart)

s1 = set()
print(s1)

s1.add("a")
s1.add('b')
s1.add('c')
print(s1)

s1.remove('b')
print(s1)

s1.clear()
print(s1)

print('a' in s1)
print('b' in s1)

a = [1,2,2,3,3,3]

print(set(a))
print(list(set(a)))

