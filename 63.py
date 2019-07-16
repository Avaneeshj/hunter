a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(a):
    c=b[i:]
    e=max(c)
    d.append(e)
f=d[0]
d.remove(f)
d.append(0)
print(*d,end="")
    
