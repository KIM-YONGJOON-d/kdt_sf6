import random
import time

# word = ["sky", "earth", "moon", "flower", "tree", "apple", "mountain", "garlic", "onion", "potato"]
with open("./words.txt", 'w') as f:
    word = ["sky", "earth", "moon", "flower", "tree", "apple", "mountain", "garlic", "onion", "potato"]
    for i in word:
        if i == word[-1]:
            f.write(i)
        else:
            f.write(i + ", ")

with open("./words.txt", 'r') as f:
    # print(f.read())
    word = f.read().split(", ")
    # print(data)
    # print(random.choice(data))

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