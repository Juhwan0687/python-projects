import turtle
from random import*
score=0
n=randint(5,10)
fruit=['apple','banana','strawberry','watermelon','mandarin','peach','grapes','orange','pear','kiwi']
flower=['rose','lily','sunflower','iris','clover','daisy','lilac','mint','ivy']
animal=['mouse','giraffe','tiger','lion','wolf','fox','monkey','dog','cat','rabbit','bear']
lists=[fruit,flower,animal]
t=turtle.Turtle('turtle')
line=turtle.Turtle()
t.speed(0)
line.setx(-200)
line.write('0')
line.setx(0)
line.write('50')
line.setx(200)
line.write('100')
t.begin_fill()
t.fillcolor('yellow')
t.setx(320)
t.right(90)
t.sety(100)
t.setx(220)
t.sety(0)
t.end_fill()
t.backward(100)
t.begin_fill()
t.fillcolor('red')
t.goto(270,200)
t.goto(320,100)
t.end_fill()
t.penup()
t.goto(20,200)
t.left(90)
t.write('김주환의 타자 게임!', font=('Arial',20,'bold'))
t.goto(0,250)
for i in range(n):
    f=choice(lists)
    s=choice(f)
    if f==fruit:
        word=turtle.textinput('fruit','%s(%d/%d)'%(s,i+1,n))
    elif f==animal:
        word=turtle.textinput('animal','%s(%d/%d)'%(s,i+1,n))
    else:
        word=turtle.textinput('flower','%s(%d/%d)'%(s,i+1,n))
    if word==s:
        score+=1
rate=score/n*100
t.penup()
t.goto(0,-50)
t.pendown()
t.write('%d/%d번 성공!'%(score,n),True,font=('Arial',15,'bold'))
t.penup()
t.goto(0,-100)
t.pendown()
t.write('정확도:%.1f%%'%(rate),True,font=('Arial',15,'bold'))
t.penup()
t.goto(-200,10)
t.pendown()
t.sety(0)
t.pencolor('skyblue')
t.pensize(10)
t.speed(1)
distance=t.distance(line)/100*rate
t.forward(distance)
if rate==100:
    t.pencolor('pink')
    t.write('집에 데려 다 줘서 고마워!',False,'center',font=('Arial',15,'bold'))
    t.left(60)
    t.right(60)
    t.left(60)
    t.right(60)
elif rate>=80:
    t.pencolor('pink')
    t.write('집이 코 앞인데!! 다시 한번만 더 시도해 줘!',False,'center',font=('Arial',15,'bold'))
elif rate>=50:
    t.pencolor('pink')
    t.write('집에 가고 싶어! ㅠ0ㅠ',False,'center',font=('Arial',15,'bold'))
else:
    t.pencolor('black')
    t.color('black')
    t.write('거북이가 쓰러졌어요! ㅠ_ㅠ',False,'center',font=('Arial',15,'bold'))
turtle.done()