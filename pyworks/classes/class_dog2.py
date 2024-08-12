# 인스턴스 변수와 클래스 변수

class Dog:
    # tricks = []
    def __init__(self, name):
        self.name = name
        self.tricks = []
        print("생성자 메서드입니다.")
    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog('John')
dog1.add_trick("몸 뒤집기")

dog2 = Dog('Jerry')
dog2.add_trick("죽은 척 하기")