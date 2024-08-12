import random
import math
print(random.random())

# dice = random.randint(1, 6)
# print(dice)

# 주사위 10번 던지기
for i in range(10):
    dice = random.randint(1, 6)
    print(dice)
# 방법 1
words = ['여름','꽃','나비','벌','나무']
print(random.choice(words))

# 방법 2
idx = words[math.floor(random.random()*len(words))]
print(idx)