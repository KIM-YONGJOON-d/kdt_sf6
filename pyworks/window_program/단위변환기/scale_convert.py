# 단위 변환기 클래스 만들기

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, value):
        return self.factor / value

    def __str__(self):
        return f'{self.units_from}, {self.units_to}, {self.factor}'
con = ScaleConverter('KB', 'MB', 1024)

if __name__ == '__main__':
    # print(con)
    print("KB를 MB로 변환")
    print(f'{con.convert(1630): .2f}{con.units_to}')