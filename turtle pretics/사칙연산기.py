def plus(w,h):
    return w+h
def minus(w,h):
    return w-h
def multiply(w,h):
    return w*h
def divide(w,h):
    return w//h
print('Choose a calculation : ')
print('1.Plus','2.Minus','3.Multiply','4.Divide',sep='\n')
n=int(input())
if n==1:
    w=int(input('Number : '))
    h=int(input('Number : '))
    area=plus(w,h)
elif n==2:
    w=int(input('Number : '))
    h=int(input('Number : '))
    area=minus(w,h)
elif n==3:
    w=int(input('Number : '))
    h=int(input('Number : '))
    area=multiply(w,h)
elif n==4:
    w=int(input('Number : '))
    h=int(input('Number : '))
    area=divide(w,h)
print(area)