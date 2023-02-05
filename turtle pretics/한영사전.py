a=str(input('단어를 입력해주세요:'))
b={'plus':'더하기, 장점','minus':'빼기, 적자','multiply':'곱하다, 다양하게','division':'나누기, 분열'}
if(a=='plus'):
    print(b['plus'])
if(a=='minus'):
    print(b['minus'])
if(a=='multiply'):
    print(b['multiply'])
if(a=='division'):
    print(b['division'])
print('\n')
print(b.keys())
b['square']='제곱'
print('\n')
print(b.items())