# 실습 1

import sys
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y
if __name__ == "__main__":
    c1 = Calculator(10, 0)
    print(c1.add())
    print(c1.sub())
    print(c1.mul())
    print(c1.div())


# 실습 2
# class SuperMarket:
#     def __init__(self, location, name, product, customer):
#         self.location = location
#         self.name = name
#         self.product = product
#         self.customer = customer
#     def show_info(self):
#         print(f'위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}')
#     def print_location(self):
#         print(f'위치: {self.location}')
#     def change_category(self,change_product):
#         self.product = change_product
#     def show_list(self):
#         print(f'상품: {self.product}')
#     def enter_customer(self):
#         self.customer += 1
# if __name__ == "__main__":
#     sm1 = SuperMarket('마포구 염리동', '마켓온', '음료수', 11)
#     sm1.enter_customer()
#     sm1.change_category('음료')
#     sm1.print_location()
#     sm1.show_list()
#     sm1.show_info()



