a=int(input())
b=list(map(int,input().split()))
c=[]
d=1
e=[]
for i in range(a):
    c=b[:i]+b[i+1:]
    for j in c:
        d*=j
    e.append(d)
    d=1
print(*e,end="")
