# 모듈 불러오기
from classes.class_quiz import Calculator
import sys

calc = Calculator(2, 3)
print(calc.add())

class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y
    def div(self):
        try:
            return self.x / self.y
        except:
            print("0으로 나눌 수 없음")
            sys.exit(0)

mc = MoreCalculator(2, 0)
print(mc.add())
print(mc.pow())
print(mc.div())