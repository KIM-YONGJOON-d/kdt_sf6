
with open('source/city.txt', 'r') as f:
    # data = f.readlines()
    a = []
    for i in range(6):
        data = f.readline().split()
        a.append(data)
    print(a)
