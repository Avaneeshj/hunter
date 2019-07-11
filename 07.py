a=int(input())
b=list(map(int,input().split()))
l=[]
m=[]
n=[]
c=0
d=1
while(c<100000):
    l.append(c)
    c+=2
while(d<100000):
    m.append(d)
    d+=2
for i in range(a):
    if((b[i] in l) and (i in m)):
        n.append(b[i])
    elif((b[i] in m) and (i in l)):
        n.append(b[i])
print(n)
