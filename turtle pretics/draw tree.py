import turtle
from random import*

t=turtle.Turtle()
t.color("#8c5d3f")
t.pensize(5)
t.left(90)
t.forward(randint(100,150))
t.left(randint(60,80))
b=randint(50,120)
t.forward(b)
t.backward(b)
t.right(randint(60,80))
t.forward(randint(50,120))
t.left(randint(60,80))
b=randint(50,120)
t.forward(b)
t.backward(b)
t.right(randint(60,80))
t.forward(randint(50,120))
t.backward(b)
t.left(randint(60,80))
b=randint(50,120)
t.forward(b)
t.backward(b)
t.right(randint(60,80))
t.forward(randint(50,120))
t.penup()
t.goto(0+100,200)
t.color("#258a45")
t.pendown()
for i in range(100):
    t.speed(100)
    t.circle(i)
    i=i-1
turtle.done()