# time.time() - 1970.1.1 자정 이후부터 시간을 초로 변환
import time
import math

# print(time.time())
#
# day = math.floor(time.time() / (24 * 60 * 60))
# print(day)
# year = math.floor(time.time() / (365 * 24 * 60 * 60))
# print(year)
start = time.time()

for i in range(1000000):
    print(i)
    # time.sleep(1)

end = time.time()
print("수행시간: " + str(end-start) + "초")