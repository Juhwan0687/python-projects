str=input('String : ')
find=input('Find Character : ')
def find_index(a,b):
    c=[]
    for i in range(len(a)):
        if a[i:]==b:
            c.append(i)
            i+=1
    return c
print(find_index(str,find))