a=int(input())
b=list(map(int,input().split()))
c=b
while(len(c)>0):
    d=len(c)
    if(d%2!=0):
        e=int(d//2)
        print(c[e])
        c.remove(c[e])
    elif(d%2==0):
        f=int(d//2)
        g=f-1
        h=int((c[f]+c[g])/2)
        print(h)
        c.remove(c[f])
        c.remove(c[g])
