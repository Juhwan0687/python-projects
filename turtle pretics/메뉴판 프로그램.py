from tkinter import*
a=[]
win=Tk()
win.title('메뉴판')
img=PhotoImage(file='샌드위치.png')
img2=PhotoImage(file='피자2.png')
img3=PhotoImage(file='파스타.png')
img4=PhotoImage(file='치킨.png')
def pizz():
    global a
    a.append('피자')
def san():
    global a
    a.append('샌드위치')
def pas():
    global a
    a.append('파스타')
def chi():
    global a
    a.append('치킨')
def f():
    global a
    a=set(a)
    list['text']=str(a)+'를 주문하셨습니다. 잠시만 기다려 주세요.'
lb1=Label(win,image=img)
lb2=Label(win,image=img2)
lb3=Label(win,image=img3)
lb4=Label(win,image=img4)
lb1.grid(row=0,column=0)
lb2.grid(row=0,column=1)
lb3.grid(row=2,column=0)
lb4.grid(row=2,column=1)
pizza=Button(win,text='피자',command=pizz)
pizza.grid(row=1,column=1)
sand=Button(win,text='샌드위치',command=san)
sand.grid(row=1,column=0)
pasta=Button(win,text='파스타',command=pas)
pasta.grid(row=3,column=0)
chicken=Button(win,text='치킨',command=chi)
chicken.grid(row=3,column=1)
주문=Button(win,text='주문하기',command=f)
주문.grid(row=4,column=1)
list=Label(win,text='',relief='sunken')
list.grid(row=5,column=0)
win.mainloop()