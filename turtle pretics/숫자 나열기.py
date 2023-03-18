n=int(input('자연수를 입력하세요.'))
c=1
def f(n,c):
    a=''
    for i in range(1,n+1):
        a+=' '
        a+=str(c*i)
    print(a)
for i in range(n):
    f(n,c+i)