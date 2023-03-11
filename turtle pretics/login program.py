def login(a,b):
    c=0
    if a!='Cube' and b!=1234:
        c=4
        return c
    if a!='Cube' and b==1234:
        c=3
        return c
    if a=='Cube' and b!=1234:
        c=2
        return c
    if a=='Cube' and b==1234:
        c=1
        return c
def say(r):
    c=''
    if r==1:
        c='Login Success.'
        return c
    elif r==2:
        c='Please Check Your PW'
        return c
    elif r==3:
        c='Please Check Your ID'
        return c
    else:
        c='Please Check Your ID and PW.'
        return c
id=str(input('ID : '))
pw=int(input('PW : '))
a=login(id,pw)
b=say(a)
print(b)