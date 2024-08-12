# 사원의 사번을 자동 부여
class Employee:
    serial_num = 1000
    def __init__(self, name):
        self.name = name
        Employee.serial_num += 1
        self.id = Employee.serial_num

    def __str__(self):
        return "사번: {1}, 이름: {0}".format(self.name, self.id)


e1 = Employee('김용준')
e2 = Employee('하기림')
e3 = Employee('이승주')
print(e1.__str__())
print(e3.__str__())
print(e2.__str__())