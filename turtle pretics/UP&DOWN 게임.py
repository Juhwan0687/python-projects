from random import*
com=randint(1,100)
user=0
while user!=com:
    user=int(input('정수를 입력하세요.'))
    if com>user:
        print('UP')
        continue
    elif com<user:
        print('DOWN')
        continue
print('Correct!')