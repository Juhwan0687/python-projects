from tkinter import*

win=Tk()
win.title('Introduce')
a=''
b=0
def nam(event):
    global a
    a=name.get()
def click():
    global b
    global a
    intro['text']='My name is '+a+', '+"and I'm "+str(b)+' years old.'
def ag(event):
    global b
    b=age.get()
lb1=Label(win,text='Name : ')
lb1.grid(row=0,column=0)
name=Entry(win,width=30)
name.bind('<Motion>',nam)
name.grid(row=0,column=1)
lb2=Label(win,text='Age : ')
lb2.grid(row=1,column=0)
lb3=Label(win,bitmap='info')
lb3.grid(row=2,column=0)
btn=Button(win,text='OK',command=click)
btn.grid(row=3,column=1)
age=Entry(win,width=30)
age.bind('<Motion>',ag)
age.grid(row=1,column=1)
intro=Label(win,text='',relief='solid',width=30)
intro.grid(row=2,column=1)
win.mainloop()