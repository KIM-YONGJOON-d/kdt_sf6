# 클래스 생성과 사용
# 클래스의 구성 요소 - 속성(멤버변수), 메서드(함수)
class Car:
    model = ""
    cc = 0
    def get_info(self):
        print("모델명:", self.model, "배기량:", self.cc)



car1 = Car()
print(car1)

car1.model = "아반떼"
car1.cc = 1500

car2 =Car()
car2.model = "BMW"
car2.cc = 2000
car2.get_info()