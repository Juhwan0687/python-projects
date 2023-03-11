a=[]
b=[]
def is_prime(a,b):
    for i in range(2,50):
        for j in range(2,50):
            a.append(i*j)
    for t in range(2,101):
        b.append(t)
    a=set(a)
    b=set(b)
    c=0
    c=b-a
    return c
print(str(is_prime(a,b)))