# 변수의 유효범위(생명주기)
# 전역변수 - 전체에 영향을 미침, 프로그램이 종료되면 메모리에서 소명
# 지역변수 - 함수나 제어문 내에서만 생성되고 소명

def get_price():
    price = 4000 * quantity
    return price

quantity = 2
order_price = get_price()

print(f'{quantity}개에 {order_price}원 입니다.')

def one_up():
    x = 0
    x= x+1
    return x
print(one_up())