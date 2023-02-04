from random import*
a=['앞면','뒷면']
n=int(input('\n동전을 던질 횟수를 입력해주세요. '))
k=[]
f=''
e=n
while n>=0:
    f=choice(a)
    if f=='앞면':
        k.append('앞면')
    else:
        k.append('뒷면')
    n-=1
g=k.count('앞면')
v=k.count('뒷면')
print('앞면 : %d회   확률 : %.3f%%'%(g,g/e*100))
print('뒷면 : %d회   확률 : %.3f%%\n'%(v,v/e*100))