count=0
n=int(input('정수를 입력하세요.'))
while True:
    count+=1
    n//=10
    if n<=0:
        break
print('\n자릿수 : %d\n'%count)