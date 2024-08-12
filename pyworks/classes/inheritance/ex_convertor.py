# 단위 변환기 확장 클래스
from class_scale_convertior import ScaleConvertor
class Convertor(ScaleConvertor):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset
    def convert(self, value):
        return value * self.factor + self.offset

    def __str__(self):
        return f'{self.units_from}, {self.units_to}, {self.factor}, {self.offset}'

con_v = Convertor('C', 'F', 1.8, 32)
print(con_v)
print(f'33{con_v.units_from} = {con_v.convert(33)}{con_v.units_to}')