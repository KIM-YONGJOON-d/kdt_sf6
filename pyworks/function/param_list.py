# 리스트를 매개 변수로 사용하는 함수

def times(a):
    # a2 =[]
    # for i in a:
    #     a2.append(i*3)
    a2 = [i*3 for i in a]
    return a2

v=[1, 2, 3, 4]
v2 = times(v)
print(v2)

