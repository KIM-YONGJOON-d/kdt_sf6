
'''
for a in range(1,10):
    for b in range(1,10):
        print(a*b,end=' ')
    print('')


for a in range(1,10):
    for b in range(1,a+1):
        print('*',end='')
    print('')
'''

# 파이썬의 단일 for
for i in range(1, 5):
    print("*" *(5-i))


for i in range(1,5):
    print(" "*(4-i) + "*"* i)


# 숫자가 연속으로 증가하는 알고리즘
for i in range(0, 4):
    for j in range(1, 5):
        print(i*4+j,end=' ')
    print()