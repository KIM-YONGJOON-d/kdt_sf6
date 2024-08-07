# global - 전역 변수임을 알려주는 키워드

def one_up():
    global x
    x += 1
    return x

x=0
print(one_up())
print(one_up())
print(one_up())