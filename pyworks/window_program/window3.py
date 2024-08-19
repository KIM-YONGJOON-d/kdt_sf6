from tkinter import *

def click():
    label.config(text = "안녕~ 파이썬!")

root = Tk()
root.title("윈도우3")
root.geometry("300x150")
root.option_add('*Font', '맑은고딕 15')

frame = Frame(root)
frame.pack()

Label(frame, text="Hello~ Python!!").grid(row=0, column=0)
Button(frame, text="확인", command = click).grid(row=1, column=0)
label = Label(frame, text="")
label.grid(row=2, column=0)

root.mainloop()