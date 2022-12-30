import turtle
from random import*

t=turtle.Turtle()
t.shape('turtle')

t.circle(randint(0,100))
t.dot(randint(1,20))
t.pensize(randint(1,10))
t.setheading(randint(0,360))
t.forward(randint(0,100))
t.backward(randint(0,100))
t.setx(randint(0,300))
t.sety(randint(0,300))

turtle.done()