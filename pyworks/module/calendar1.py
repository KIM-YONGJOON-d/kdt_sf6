import calendar as cal
import datetime as dt

cal.prcal(2024)

# 2024년 8월
cal.prmonth(2024, 8)

# 2024년 8월 12일 요일
print(cal.weekday(2024, 8, 12))

# 날짜로 요일 알아내기 - 숫자 인덱스를 요일로 바꾸기
days = ['월', '화', '수', '목', '금', '토', '일']
weekday = dt.date.today().weekday()
print(f'오늘은 {days[weekday]}요일입니다.')

# 8월 15일의 요일은?
day815 = dt.date(2024, 8, 15).weekday()
print(f'광복절은 {days[day815]}요일입니다.')

# 날짜를 입력하면 요일을 추력하는 함수 정의
def get_weekday(yyyy, mm , dd):
    print(f'{yyyy}년 {mm}월 {dd}일 {days[dt.date(yyyy, mm, dd).weekday()]}요일')

get_weekday(2024, 8, 15)