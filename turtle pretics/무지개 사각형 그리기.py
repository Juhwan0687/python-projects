import turtle
t=turtle.Turtle('turtle')
t.pensize(20)
t.speed(0)
color=['red','orange','yellow','green','blue','dark blue','purple']
i=100
k=1
j=1
for k in range(7):
    t.pencolor(color[k])
    for j in range(4):
        t.forward(i)
        t.right(90)
        j+=1
    t.penup()
    k+=1
    t.sety(k*20)
    t.setx(0-k*20)
    i+=40
    t.pendown()
t.penup()
t.goto(0-k*20+20,-50)
t.pendown()
t.goto(k*20+80,-50)
t.penup()
t.goto(50,k*20-20)
t.setheading(90)
t.pendown()
t.goto(50,0-k*20-80)
turtle.done()