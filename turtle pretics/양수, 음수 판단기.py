def judge(n):
    if n>0:
        print('\nPlus\n')
    elif n<0:
        print('\nMinus\n')
    else:
        print('\nZero\n')
n=int(input('정수를 입력하세요.'))
judge(n)