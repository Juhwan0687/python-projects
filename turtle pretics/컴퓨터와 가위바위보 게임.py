from random import*
a=['가위','바위','보']
user=input('\n가위, 바위, 보 중 선택해 내십시오.')
com=choice(a)
if com==user:
    print('COM : %s     Draw!'%(com))
elif com=='가위' and user=='바위':
    print('COM : %s     You Win!'%(com))
elif com=='바위' and user=='가위':
    print('COM : %s     COM Win!'%(com))
elif com=='바위' and user=='보':
    print('COM : %s     You Win!'%(com))
elif com=='보' and user=='바위':
    print('COM : %s     COM Win!'%(com))
elif com=='가위' and user=='보':
    print('COM : %s     COM Win!'%(com))
else:
    print('COM : %s     You Win!'%(com))