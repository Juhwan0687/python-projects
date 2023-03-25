from tkinter import*

win=Tk()
win.title('Grid')

lb1=Label(win,width=10,height=5,bg='red')
lb2=Label(win,width=10,height=5,bg='orange')
lb3=Label(win,width=10,height=5,bg='yellow')
lb4=Label(win,width=10,height=5,bg='green')
lb5=Label(win,width=10,height=5,bg='blue')
lb6=Label(win,width=10,height=5,bg='purple')

lb1.grid(row=0,column=0)
lb2.grid(row=0,column=1)
lb3.grid(row=0,column=2)
lb4.grid(row=1,column=0)
lb5.grid(row=1,column=1)
lb6.grid(row=1,column=2)

win.mainloop()