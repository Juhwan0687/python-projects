n=int(input('정수를 입력하세요.'))
for i in range(n+1):
    print('*'*i)
for j in range(1,n+1):
    print(' '*(n-j),end='*'*j)
    print()