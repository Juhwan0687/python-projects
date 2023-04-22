from tkinter import*
win=Tk()
win.geometry('300x300+100+100')
def aca(n):
    if n==0:
        lb1['image']=PhotoImage('alien.png')
    else:
        lb1['image']=PhotoImage('alien2.png')
def acf(n):
    if n==0:
        lb2['image']=PhotoImage('frank.png')
    else:
        lb2['image']=PhotoImage('frank2.png')
ac1=Button(win,text='Action1',command=aca(0))
ac2=Button(win,text='Action2',command=aca(1))
fc1=Button(win,text='Action1',command=acf(0))
fc2=Button(win,text='Action2',command=acf(1))
lb1=Label(image=PhotoImage('alien.png'))
lb2=Label(image=PhotoImage('frank.png'))
lb1.grid(row=0,column=0,columnspan=3)
lb2.grid(row=0,column=1)
ac1.grid(row=1,column=0,columnspan=3)
ac2.grid(row=1,column=1)
fc1.grid(row=1,column=2)
fc2.grid(row=1,column=3)
win.mainloop()