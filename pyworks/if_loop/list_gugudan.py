# 구구단 프로그램 구현 - 리스트

# dan = 2
# gugu = []
# for i in range(1, 10):
#     gugu.append(dan * i)
#     print(f'{dan} x {i} = {gugu[i-1]}')
# print(gugu)

# 구구단 전체 출력
gugudan = []
for i in range(2, 10):
    row = []
    for j in range(1, 10):
        row.append(i*j)
        print(f'{i} x {j} = {row[j-1]}')
    # print(row)
    print()