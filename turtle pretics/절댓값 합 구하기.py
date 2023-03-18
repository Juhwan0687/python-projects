a=int(input('정수를 입력하세요.'))
b=int(input('정수를 입력하세요.'))
c=int(input('정수를 입력하세요.'))
d=int(input('정수를 입력하세요.'))
e=int(input('정수를 입력하세요.'))
f=0
list=[a,b,c,d,e]
def 절댓값(n):
    if n>0:
        b=str(n)
        return b[0:]
    elif n<0:
        b=str(n)
        return b[1:]
    else:
        return 0
for i in range(0,5):
    f+=int(절댓값(list[i]))
print(f)