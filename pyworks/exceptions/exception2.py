
def divide(x, y):
    try:
        result = x / y
        print(result)
    except ZeroDivisionError:
        print("0으로 나눌 수 없음")
    finally:
        print("여기는 반드시 수행됩니다.")

divide(2, 0)