with open("./source/data.txt", "w") as f1:
    f1.write("Hello World\n")
    f1.write("폭염이 극성이다.\n")
    num = ('1KB는 %dB이다'% 1024)
    f1.write(num)

with open("./source/data.txt", "r") as f2:
    data = f2.read()
    print(data)
