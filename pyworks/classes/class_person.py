# 정보 은닉(보안을 유지하기 위해 접근을 허용하지 않음)
# 접근 제어자 - public(기본), private, protected
# 외부로 쓰지 않고 내부적으로 작동한다
class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        print(self.__name)
    def set_age(self, age):
        self.__age = age
    def get_age(self):
        print(self.__age)
p1 = Person()
p1.set_name('김용준')
p1.get_name()
p1.set_age(25)
p1.get_age()

