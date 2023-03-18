n=int(input('자연수를 입력하세요.'))
a=0
b=''
def fibo(n):
    return fibo(n-1) + fibo(n-2) if n >= 2 else n
for i in range(1,n+1 ):
    a=fibo(i)
b=str(a)
print(b)