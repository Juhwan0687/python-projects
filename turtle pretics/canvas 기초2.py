from tkinter import*
win=Tk()
c=Canvas(win,bg='white',width=400,height=20)
c.create_line(50,10,350,10,fill='green',width=5)
c.pack(fill='both',expand=True)
win.mainloop()