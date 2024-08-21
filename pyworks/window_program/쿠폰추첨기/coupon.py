# 쿠폰 추첨기
# 추첨 버튼을 누르면 3명이 랜덤하게 출력 됨
from tkinter import *
import random

def click():
    name_list = ['김용준', '김용혁', '임현수', '윤종관', '정지은', '오민선', '최준영',
                 '윤다빈', '박민우', '조형주', '고지수']
    choice_list = []
    while len(choice_list) < 3:
        choice = random.choice(name_list)
        if choice not in choice_list:
            choice_list.append(choice)
    # choice_list = set()
    # while len(choice_list) < 3:
    #     choice = random.choice(name_list)
    #     choice_list.add(choice)

    text.delete('0.0', END)
    text.insert(END, choice_list)


window = Tk()
window.title('쿠폰 추첨기')

# 이미지 객체 생성
lbl_img = Label(window)
# 이미지 넣기
img = PhotoImage(file='bronx.png')
lbl_img.config(image=img)
lbl_img.grid(row=0, column=0, sticky=W)


Button(window, text="추첨", command=click).grid(row=1, column=0, sticky=E)

text = Text(window, width=47, height=3, bg='yellow')
text.grid(row=2, column=0, sticky=W)

window.mainloop()