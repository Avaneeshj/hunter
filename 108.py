a=list(input())
z=len(a)
c=[]
d=a
e=a[0]
d.append(e)
if(z==1):
    print(int(a[0])*int(a[0]))
else:
    for i in range(len(a)-1):
        f=int(d[i])
        g=int(d[i+1])
        c.append(f**g)
    print(sum(c))
