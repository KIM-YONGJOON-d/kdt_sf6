
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

c1 = Calculator(10, 5)

print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.div())


