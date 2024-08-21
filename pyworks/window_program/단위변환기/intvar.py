from tkinter import *

def click():
    result = value.get()
    text.delete(0.0, END)
    text.insert(END, result)

root = Tk()
root.title("정수형 변수")
root.geometry('200x100')

# 정수형 변수 선언
# value = 10 (콘솔에서 변수)
value = IntVar()
value.set(10)

Button(root, text="확인", command=click).grid(row=0, column=0)

text = Text(root, width=10, height=2)
text.grid(row=1, column=0)


root.mainloop()