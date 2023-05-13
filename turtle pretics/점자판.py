from tkinter import*

win=Tk()
c=Canvas(win,width=150,height=150,bg='white')
c.pack()

x1,y1=25,25
x2,y2=25,125

for i in range(11):
    c.create_line(x1,y1,x2,y2,fill='black',width=3)
    x1,x2=x1+10,x2+10

x1,x2=25,125
y1,y2=25,25

for j in range(11):
    c.create_line(x1,y1,x2,y2,fill='black',width=3)
    y1=y1+10
    y2=y2+10

#c.create_oval(45,45,105,105,fill='blue',outline='black')

#c.create_oval(55,55,95,75,fill='red',outline='black')

#c.create_rectangle(35,35,105,75,fill='yellow',outline='black')

#c.create_polygon(75,35,35,115,115,115,fill='red',outline='black')

win.mainloop()