a=int(input())
b=list(map(int,input().split()))
c=[]
e=[]
f=[]
for i in range(a):
    for j in range(a):
        if(j>i):
            d=abs(b[i]+b[j])
            e.append(b[i])
            f.append(b[j])
            c.append(d)
g=min(c)
h=c.index(g)
print(e[h],f[h])
