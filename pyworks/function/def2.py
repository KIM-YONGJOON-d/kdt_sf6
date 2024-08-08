# return 이 있는 함수(반환 값이 있음)
# 매개변수 1개
def square(x):
    return x*x

def myabs(x):
    if x < 0:
        return -x
    else:
        return x

def mul(x, y):
    return  x*y


value = square(6)
print(value)

print(myabs(-10))

print(mul(3, 5))


