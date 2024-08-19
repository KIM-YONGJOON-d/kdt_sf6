# 윈도우 생성 - tkinter
# 체계 : root=TK() > Frame() > Label(), Button()
# import tkinter as tk

from tkinter import *
root = Tk()
root.title("처음 만든 윈도우")
root.geometry('200x100')

Label(root, text="안녕하세요~").grid(row=0, column=0, sticky=E)
Button(root, text="확인").grid(row=1, column=1, sticky=E)

root.mainloop()