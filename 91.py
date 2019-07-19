from itertools import permutations
a=input()
z=tuple(a)
d=0
c=[]
b=permutations(a)
if(len(a)==1):
    d=1
else:
    for i in list(b):
        c.append(i)
    for i in range(len(c)):
        if(c[i]==z):
            d=0
        else:
            d+=1
            break
if(d>0):
    print("yes")
else:
    print("no")
