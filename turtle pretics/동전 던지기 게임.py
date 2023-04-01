from tkinter import*
from random import*

win=Tk()

win.title('동전 던지기 게임')

def game(com,user):
    if com==user:
        lb1_res['text']='Correct!'
    else:
        lb1_res['text']='Incorrect..'

def change_img(user):
    list=['coinfront.png','coinback.png']

    com=randint(0,1)

    com_img=PhotoImage(file=list[com])
    lb1['image']=com_img
    lb1.image=com_img

    game(com,user)

basic_img=PhotoImage(file='ready.png')
com_img=PhotoImage()

lb1=Label(win,image=basic_img,relief='solid')
lb1_res=Label(win,font=('consolas',20,'bold'),fg='orange')
front=Button(win,text='Front',bg='skyblue',font=('consolas',20,'bold'),command=lambda:change_img(0))
back=Button(win,text='Back',bg='lightpink',font=('consolas',20,'bold'),command=lambda:change_img(1))

lb1.pack()
lb1_res.pack()
front.pack(side=LEFT)
back.pack(side=RIGHT,)

win.mainloop()