import random

lotto = []
while len(lotto) < 6:
    a = random.randint(1, 45)
    if a not in lotto:
        lotto.append(a)

lotto.sort()
print(lotto)

