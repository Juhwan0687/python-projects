b=[]
a=int(input('정수를 입력하세요.'))
c=int(input('정수를 입력하세요.'))
b.append(c)
b.append(a)
if b[0]>b[1]:
    del(b[1])
else:
    del(b[0])
for i in range(8):
    a=int(input('정수를 입력하세요.'))
    b.append(a,)
    if b[0]>b[1]:
        del(b[1])
    else:
        del(b[0])
print(b)