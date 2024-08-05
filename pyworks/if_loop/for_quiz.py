# 실습1
'''
sum = int(input("어디까지 계산할까요? "))

for i in range(1,sum):
    sum+=i
print(sum)
'''

# 실습
count = int(input("몇초? "))
for i in range(0, count):
    print(count, end=" ")
    count-=1
print("발사!")

