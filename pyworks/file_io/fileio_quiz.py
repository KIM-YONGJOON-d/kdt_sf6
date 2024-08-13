
f = open("c:/pyfile/gugudan.txt", "w")
for i in range(2,10):
    for j in range(1,10):
        a = f"{i} x {j} = {i*j}\n"
        f.write(a)
f.close()

f = open("c:/pyfile/gugudan.txt", "r")
print(f.read())
f.close()