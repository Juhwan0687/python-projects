from random import*
com=randint(1,100)
user=0
a=0
c=0
while com!=user:
    user=int(input())
    if user>com:
        print('Up Or Down? DOWN')
        a+=1
    elif user<com:
        print('Up Or Down? UP')
        a+=1
    else:
        print('Up Or Down? Correct!')
        a+=1
        print('NUMBER : %d      TRIES : %d'%(com,a))