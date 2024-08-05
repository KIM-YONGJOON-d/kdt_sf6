# for 반복문
'''
for i range

'''

'''
a = range(10)
print(list(a))

b = range(1, 11)
print(list(b))

c = range(1, 11, 2)
print(list(c))

for i in range(1, 11):
    print(i)
'''
total = 0
for i in range(1, 11):
    total +=i
    print("i=",i, "total=",total)