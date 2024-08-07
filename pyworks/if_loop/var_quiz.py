# 실습2
def get_price(price, count):
    if price * count < 20000:
        return price*count + 2500
    else:
        return price*count

print(f"상품1 가격: {format(get_price(10000,3),',d')}원")
print(f"상품2 가격: {format(get_price(5500,3),',d')}원")