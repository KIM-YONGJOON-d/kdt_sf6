# # 예외 미루기
#
# class Animal:
#     def breathe(self):
#         print("동물이 숨을 쉰다")
#
#     def cry(self):
#         raise NotImplementedError
#
# class Dog(Animal):
#     def sleep(self):
#         print("강아지가 잠을 잔다.")
#     def cry(self):
#         print("멍멍")
#
# dog = Dog()
# dog.breathe()
# dog.sleep()
# dog.cry()
#
# # 고양이 클래스 구현
# class Cat(Animal):
#     def sleep(self):
#         print("고양이가 잠을 잔다.")
#     def cry(self):
#         print("냥냥")
#
# cat = Cat()
# cat.breathe()
# cat.sleep()
# cat.cry()

# 입력 받을 때 에러 처리
try:
    num = int(input("숫자 입력: "))
except ValueError as e:
    print(e)
