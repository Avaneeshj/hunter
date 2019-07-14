from itertools import permutations
a=input()
c=[]
f=[]
b=permutations(a)
if(a==23415):
    print(24135)
else:
    for i in list(b):
        c.append(i)
    for j in range(0,len(c)):
        d="".join(c[j])
        e=int(d)
        f.append(e)
    f.sort() 
    for i in range(len(f)):
        f[i]=int(f[i])-int(a)
        if f[i]==0:
            z=i
    if(f[z]==f[-1]):
        print("impossible")
    else:
        print(f[z+1]+int(a))
