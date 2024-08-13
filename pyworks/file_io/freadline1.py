
f = open("c:/pyfile/file1.txt", "r")
line1 = f.readline()
print(line1)
while True:
    line = f.readline()
    if not line:
        break
    print(line.strip())
f.close()