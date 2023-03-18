n=float(input('소수를 입력하세요.'))
def point(n):
    a=str(n)
    b=a.find('.')
    print(a[b+1:])
point(n)