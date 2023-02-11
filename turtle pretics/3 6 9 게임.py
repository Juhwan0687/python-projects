n=1
while n<=20:
    n=str(n)
    if n[1:]=='3' or n[1:]=='6' or n[1:]=='9' or n[0:]=='3' or n[0:]=='6' or n[0:]=='9':
        print('X',end=' ')
    else:
        print(n,end=' ')
    n=int(n)
    n+=1