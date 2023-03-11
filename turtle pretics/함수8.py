def get_max(n):
    s=[]
    for i in range(n):
        s.append(int(input()))
    a=set(s)
    b=list(a)
    return str(b[n-1:])
n=int(input('Enter Integer n : '))
print('max value : %s'%(get_max(n)))