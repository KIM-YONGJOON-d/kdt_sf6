# 실습 5
# sum()
# print(sum([1,2,3]))
# print(max([1,2,3]))

input_num = input("숫자 여러 개 입력").split(" ")
numbers = []
for i in input_num:
    numbers.append(int(i))
print(numbers)
max_num=max(numbers)
min_num=min(numbers)
print(f"가장 큰 값: {max_num}")
print(f"가장 작은 값: {min_num}")
avg_num = (sum(numbers)-(max_num+min_num))/(len(numbers)-2)
print(f"나머지 값의 평균: {avg_num}")


