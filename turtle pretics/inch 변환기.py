from tkinter import*

win=Tk()
win.title('단위 변환기')
def f(event):
    a=0
    a=entry.get()
    b=0.0
    b=float(a)*3.9
    lb3['text']=b

entry=Entry(win)
entry.bind('<Return>',f)
lb1=Label(win,text='cm 입력 :')
lb1.grid(row=0,column=0)
lb2=Label(win,text='inch :')
lb2.grid(row=1,column=0)
lb3=Label(win,text='')
lb3.grid(row=1,column=1)
entry.grid(row=0,column=1)
win.mainloop()