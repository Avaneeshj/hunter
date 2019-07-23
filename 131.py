a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
z=[]
l=[]
y=a//2
for i in range(a):
    z.append(b[i])
e=int(a//2)
for i in range(a):
    f=max(b)
    c.append(max(b))
    b.remove(f)
for i in range(a):
    g=min(z)
    d.append(min(z))
    z.remove(g)
for i in range(y):
    for j in range(y):
        if i==j:
            l.append(c[i])
            l.append(d[j])
            x=i
if a%2!=0:
    l.append(c[x+1])
print(*l)
