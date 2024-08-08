# 생성자(constructor)

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def show_info(self):
        print(f"모델명: {self.model}, 연식: {self.year}")

'''

car_a = Car('아이오닉6', 2023)
car_a.show_info()

car_b = Car('스포티지', 2020)
car_b.show_info()
'''

cars = [
    Car("소나타", 2020),
    Car("K5", 2017),
    Car("모닝", 2022)
]
cars[0].show_info()
print("****** 승용차 List ******")
for car in cars:
    car.show_info()