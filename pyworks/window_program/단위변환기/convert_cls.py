from tkinter import *
from window_program.단위변환기.scale_convert import ScaleConverter

class App:
    def __init__(self, root):
        self.conv = ScaleConverter('KB', 'MB', 1024)
        frame = Frame(root)
        frame.pack()

        Label(frame, text="KB").grid(row=0,column=0)
        self.kb = IntVar()
        # textvariable = 객체(멤버) 변수, "KB"입력
        Entry(frame, textvariable=self.kb).grid(row=0, column=1)
        Label(frame, text="MB").grid(row=1, column=0)
        # "MB"출력 - 레이블
        self.mb = DoubleVar()
        Label(frame, textvariable=self.mb).grid(row=1, column=1)
        Button(frame, text="변환", command=self.convert).grid(row=2, columnspan=2)

    def convert(self):
        kb = self.kb.get()
        mb = self.conv.convert(kb)
        mb = f'{mb:.2f}'
        self.mb.set(mb)


root = Tk()
root.title("단위 변환기")
root.geometry("300x100+200+200")

app=App(root)

root.mainloop()