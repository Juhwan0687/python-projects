d=[]
for i in range(5):
    a=str(input('정수를 2개 입력하세요.'))
    b=int(a[0:a.index(' ')])
    c=int(a[a.index(' '):])
    if b-c==2 or c-b==2:
        d.append(b+c)
print(d)