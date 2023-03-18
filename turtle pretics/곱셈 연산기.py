n=int(input('정수를 입력하세요.'))
f=int(input('정수를 입력하세요.'))
def times_table(n,f):
    for i in range(1,10):
        print('%d * %d = %d'%(n,i,n*i))
    print('\n==%d Times=='%f)
    for i in range(1,10):
        print('%d * %d = %d'%(f,i,f*i))
print('\n==%d Times=='%n)    
times_table(n,f)