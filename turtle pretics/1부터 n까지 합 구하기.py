n=int(input('자연수를 입력하세요.'))
def f(n):
    if n==1:
        return 1
    else:
        return n+f(n-1)
print(f(n))