import datetime

now = datetime.datetime.now()

print(now)

print(f'{now.hour}:{now.minute}:{now.second}')

the_day = datetime.date(2024, 7, 31)
print(the_day)

today = datetime.date.today()
print(today)

print(" ★ 지금까지 몇 일? ★ ")
passed_time = today - the_day
print(passed_time)
print(f'개강 이후 {passed_time.days}일 지났습니다')

# 추석까지 D-day
chuseock = datetime.date(2024, 9, 17)
to_chuseock = chuseock - today
print(f'추석까지 D-{to_chuseock.days}')

