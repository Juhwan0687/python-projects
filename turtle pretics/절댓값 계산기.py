n=int(input('정수를 입력하세요.'))
def 절댓값(n):
    if n>0:
        b=str(n)
        print(b[0:])
    elif n<0:
        b=str(n)
        print(b[1:])
    else:
        print(0)
절댓값(n)