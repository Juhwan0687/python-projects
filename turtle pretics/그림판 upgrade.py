from tkinter import*

canvas_color='white'
pen_color='black'
width=2
fill_color='white'
click=False
click2=False
click3=False
shape=1

def paint(event):
    global pen_color
    x1,y1=event.x,event.y
    x2,y2=x1+5,y1+5
    c.create_line(x1,y1,x2,y2,width=width,fill=pen_color)

def change_color(color):
    global pen_color
    global canvas_color
    global click
    global click2
    global click3
    global fill_color

    if click3==True:
        fill_color=color
        if fill_color=='black':
            fill_color_btn['fg']='white'
        else:
            fill_color_btn['fg']='black'
        fill_color_btn['bg']=fill_color
        click3=False

    elif click2==True:
        pen_color=color
        if pen_color=='black':
            pen_color_btn['fg']='white'
        else:
            pen_color_btn['fg']='black'
        pen_color_btn['bg']=pen_color
        click2=False

    if click==True:
        canvas_color=color
        c['bg']=canvas_color
        if canvas_color=='black':
            canvas_color_btn['fg']='white'
        else:
            canvas_color_btn['fg']='black'
        canvas_color_btn['bg']=canvas_color
        click=False
    
def change_width(event):
    global width
    if event=='+':
        width+=1
    else:
        width-=1

    if width<1:
        width=1
    
def change_canvas_color():
    global click
    click=True

def change_pen_color():
    global click2
    click2=True

def change_fill_color():
    global click3
    click3=True

def change_shape(x):
    global shape
    if x==1:
        shape=1
    elif x==2:
        shape=2
    else:
        shape=3

def create(event):
    global fill_color
    global width
    global c
    global shape
    global pen_color
    print(shape)
    if shape==1:
        c.create_oval(event.x-width,event.y-width,event.x+width,event.y+width,fill=fill_color,outline=pen_color)
    elif shape==2:
        c.create_rectangle(event.x-width,event.y-width,event.x+width,event.y+width,fill=fill_color,outline=pen_color)
    elif shape==3:
        c.create_polygon(event.x,event.y-width//2,event.x-width//2,event.y+width//2,event.x+width//2,event.y+width//2,fill=fill_color,outline=pen_color)

win=Tk()
win.title('그림판')
c=Canvas(win,bg='white',width=500,height=500)

white_btn=Button(win,text='White',height=3,width=15,bg='white',command=lambda:change_color('white'),font=('consolas',15,'bold'))
black_btn=Button(win,text='Black',height=3,width=15,bg='black',fg='white',command=lambda:change_color('black'),font=('consolas',15,'bold'))
blue_btn=Button(win,text='Blue',height=3,bg='blue',width=15,fg='white',command=lambda:change_color('blue'),font=('consolas',15,'bold'))
green_btn=Button(win,text='Green',height=3,bg='Green',width=15,fg='white',command=lambda:change_color('green'),font=('consolas',15,'bold'))
yellow_btn=Button(win,text='Yellow',height=3,bg='yellow',width=15,command=lambda:change_color('yellow'),font=('consolas',15,'bold'))
red_btn=Button(win,text='Red',bg='red',height=3,width=15,command=lambda:change_color('red'),font=('consolas',15,'bold'))
plus_btn=Button(win,text='+',height=3,width=15,command=lambda:change_width('+'),font=('consolas',15,'bold'))
minus_btn=Button(win,text='-',height=3,width=15,command=lambda:change_width('-'),font=('consolas',15,'bold'))
clear_btn=Button(win,text='Clear',height=3,width=15,command=lambda:c.delete('all'),font=('consolas',15,'bold'))
canvas_color_btn=Button(win,text='Canvas color',width=15,height=3,bg=canvas_color,command=lambda:change_canvas_color(),font=('consolas',15,'bold'))
pen_color_btn=Button(win,text='Pen color',width=15,height=3,bg=pen_color,fg='white',command=lambda:change_pen_color(),font=('consolas',15,'bold'))
fill_color_btn=Button(win,text='Fill color',width=15,height=3,bg=pen_color,fg='white',command=lambda:change_fill_color(),font=('consolas',15,'bold'))
circle_btn=Button(win,text='circle',width=15,height=3,fg='black',font=('consolas',15,'bold'),command=lambda:change_shape(1))
rect_btn=Button(win,text='rect',width=15,height=3,fg='black',font=('consolas',15,'bold'),command=lambda:change_shape(2))
tri_btn=Button(win,text='tri',width=15,height=3,fg='black',font=('consolas',15,'bold'),command=lambda:change_shape(3))

c.grid(row=0,column=0,columnspan=6)

tri_btn.grid(row=3,column=3)
rect_btn.grid(row=3,column=2)
circle_btn.grid(row=3,column=1)
canvas_color_btn.grid(row=1,column=0)
fill_color_btn.grid(row=3,column=0)
pen_color_btn.grid(row=2,column=0)
white_btn.grid(row=2,column=1)
black_btn.grid(row=1,column=1)
blue_btn.grid(row=1,column=2)
green_btn.grid(row=1,column=3)
yellow_btn.grid(row=2,column=3)
red_btn.grid(row=2,column=2)
plus_btn.grid(row=1,column=4)
minus_btn.grid(row=2,column=4)
clear_btn.grid(row=3,column=4)

c.bind('<B1-Motion>',paint)
c.bind('<Double-Button-1>',create)

win.mainloop()