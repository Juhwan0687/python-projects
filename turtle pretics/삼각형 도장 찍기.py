from tkinter import*

def draw_shape(event):
    x1,y1=event.x,event.y-12.5
    x2,y2=event.x-25,event.y+12.5
    x3,y3=event.x+25,event.y+12.5
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,outline='black',fill='green')

win=Tk()
canvas=Canvas(win,height=300,width=300)
canvas.pack()

canvas.bind('<Double-Button-1>',draw_shape)

win.mainloop()