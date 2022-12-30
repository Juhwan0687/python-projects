import turtle
from random import*

t=turtle.Turtle()
t.shape('turtle')

x=randint(0,300)
y=randint(0,300)

t.goto(x,y)

x=random()+randint(0,300)
y=random()+randint(0,300)

t.goto(x,y)

x=random()+randint(0,300)
y=random()+randint(0,300)

t.goto(x,y)

turtle.done()