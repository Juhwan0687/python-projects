import turtle
from random import*
c=('red','yellow','orange','green','blue','purple','pink')
t=turtle.Turtle()
a=randint(0,6)
t.fillcolor(c[a])
b=randint(10,100)
t.begin_fill()
t.circle(b)
t.end_fill()
t.forward(110)
a=randint(0,6)
t.fillcolor(c[a])
b=randint(10,100)
t.begin_fill()
t.circle(b)
t.end_fill()
t.forward(110)
a=randint(0,6)
t.fillcolor(c[a])
b=randint(10,100)
t.begin_fill()
t.circle(b)
t.end_fill()
t.forward(110)
a=randint(0,6)
t.fillcolor(c[a])
b=randint(10,100)
t.begin_fill()
t.circle(b)
t.end_fill()
turtle.done()