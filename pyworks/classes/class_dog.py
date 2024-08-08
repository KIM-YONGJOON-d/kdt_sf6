class Dog:
    kind = "진돗개" # 클래스 변수
    def __init__(self, name):
        self.name = name

dog1 = Dog("송이")
dog2 = Dog("백구")

print(dog1.name)
print(dog2.name)
Dog.kind = "허스키"
print(dog1.kind)