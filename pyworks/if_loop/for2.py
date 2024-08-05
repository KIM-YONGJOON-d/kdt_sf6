# for in 리스트

shop = ['반팔티', '바지', '이어폰', '키보드']

print('바지' in shop)
print('양말' in shop)
print('양말' not in shop)

shop.append('마우스')
print(shop[:])

shop.remove('이어폰')
for i in shop:
    print(i)

score = [70,80,60,90,40]

print(len(score))
print(sum(score))

print(f'개수: {len(score)}')
print(f'합계: {sum(score)}')
print(f'평균: {sum(score)/len(score)}')
print(f'최대값: {max(score)}')
print(f'최소값: {min(score)}')

# 합계
sum_v = 0
for i in score:
    sum_v += i
print(f'합계: {sum_v}')

# 최대값
max_v = score[0]
for i in score:
    if max_v < i:
        max_v = i
print(f'최대값: {max_v}')

# 최소값
min_v = score[0]
for i in score:
    if min_v > i:
        min_v = i
print(f'최소값: {min_v}')


