# 단위 변환기 클래스 만들기

class ScaleConvertor:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, value):
        return self.factor*value

    def __str__(self):
        return f'{self.units_from}, {self.units_to}, {self.factor}'
con = ScaleConvertor('MB', 'KB', 1024)

if __name__ == '__main__':
    print(con)
    # print("1MB = ", end='')
    print(f'2{con.units_from} = {con.convert(2)}{con.units_to}')

    con2 = ScaleConvertor('inch', 'mm', 25.4)
    print(f'2{con2.units_from} = {con2.convert(2)}{con2.units_to}')