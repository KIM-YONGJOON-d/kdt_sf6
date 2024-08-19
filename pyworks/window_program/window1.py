# 윈도우 생성 - tkinter
# 체계 : root=TK() > Frame() > Label(), Button()
# import tkinter as tk

from tkinter import *
root = Tk()
root.title("처음 만든 윈도우")
root.geometry('200x100')

Label(root, text="안녕하세요~").pack(side=TOP)
Button(root, text="확인").pack(side=LEFT)

root.mainloop()