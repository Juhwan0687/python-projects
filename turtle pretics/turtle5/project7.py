a={'plus':'더하기, 장점','minus':'빼기, 적자','multiply':'곱하다, 다양하게','division':'나누기, 분열','square':'제곱'}
b=str(input('단어를 입력하세요:'))
if(b=='plus'):
    del a['plus']
    print(a.items())
if(b=='minus'):
    del a['minus']
    print(a.items())
if(b=='multiply'):
    del a['multiply']
    print(a.items())
if(b=='division'):
    del a['division']
    print(a.items())
if(b=='square'):
    del a['square']
    print(a.items())