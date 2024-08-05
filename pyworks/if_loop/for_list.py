# 리스트의 복사(새로운 리스트 생성)
a =[1,2,3,4]
a2=[]
a3=[]

for i in a:
    a2.append(i)
print(a2)

for i in a2:
    a3.append(i*3)
print(a3)

a4 = [i*3 for i in a2]
print(a4)

a5 = [i*3 for i in a2 if i %2==0]
print(a5)