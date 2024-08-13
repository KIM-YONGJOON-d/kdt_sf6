import random
import time
word = ["sky", "earth", "moon", "flower", "tree", "apple", "mountain", "garlic", "onion", "potato"]
n = 1
input("[타자 게임] 준비되면 엔터!")
a = time.time()
while n < 11:
    print("문제", n)
    question = random.choice(word)
    print(question)
    user = input()
    if user == question:
        print("통과!!")
        n=n+1
    else:
        print("오답!, 다시 도전!")

b = time.time()
print(f"타자 시간: {round(b-a)}초")
print("게임 종료")