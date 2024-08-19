# 이름을 입력받아서 출력하는 윈도우
from tkinter import *

def click():
    name = entry.get()
    label.config(text = name)

root = Tk()
root.title("이름 입력")
root.geometry("400x200+550+300")


frame = Frame(root)
frame.pack()

Label(frame, text="이름: ").grid(row=0, column=0)
entry = Entry(frame)
entry.grid(row=0, column=1)
Button(frame, text="확인", command = click).grid(row=1, columnspan=2)
label = Label(frame, text="")
label.grid(row=2, columnspan=2)

root.mainloop()